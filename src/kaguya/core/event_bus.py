"""
EventBus central de Kaguya IA.

Rôle:
- Permettre aux modules de communiquer sans dépendances directes.
- Publier / s'abonner à des événements typés.
- Supporter des handlers sync et async.
- Offrir une trace debug (optionnelle) du trafic d'événements.

Fichiers/Modules impactés:
- Tous les modules (brain, emotion, memory, audio, actions, ui, etc.) doivent utiliser ce bus
  au lieu d'appeler directement d'autres modules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union
import asyncio
import time
import uuid


Handler = Union[
    Callable[["Event"], Any],
    Callable[["Event"], Awaitable[Any]],
]


@dataclass(frozen=True)
class Event:
    """
    Représente un événement transitant sur le bus.

    - name: nom stable de l'événement (ex: "USER_SPOKE", "EMOTION_UPDATED")
    - payload: dictionnaire de données associées
    - event_id: id unique pour corrélation logs/debug
    - ts_ms: timestamp en millisecondes
    - source: module source (ex: "audio.stt")
    """
    name: str
    payload: Dict[str, Any] = field(default_factory=dict)
    source: str = "unknown"
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    ts_ms: int = field(default_factory=lambda: int(time.time() * 1000))


class EventBus:
    """
    Bus d'événements simple, robuste, thread-friendly (via loop asyncio).

    Fonctionnement:
    - subscribe(event_name, handler): enregistre un handler
    - publish(event): déclenche tous les handlers de cet event_name
    - wildcard: possibilité de s'abonner à "*" pour tout recevoir (debug/trace)

    Notes:
    - On supporte handlers sync ET async.
    - En cas d'erreur d'un handler: l'erreur est remontée au caller (ou collectée si publish(..., swallow=True)).
    """

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Handler]] = {}
        self._lock = asyncio.Lock()

    async def subscribe(self, event_name: str, handler: Handler) -> None:
        """
        Abonne un handler à un événement.

        - event_name: nom exact ou "*" pour tout.
        - handler: fonction sync ou async.
        """
        async with self._lock:
            self._subscribers.setdefault(event_name, []).append(handler)

    async def unsubscribe(self, event_name: str, handler: Handler) -> None:
        """Retire un handler."""
        async with self._lock:
            if event_name in self._subscribers:
                self._subscribers[event_name] = [h for h in self._subscribers[event_name] if h != handler]
                if not self._subscribers[event_name]:
                    del self._subscribers[event_name]

    async def publish(self, event: Event, *, swallow: bool = False) -> List[Any]:
        """
        Publie un événement.

        - swallow=False: la première exception stoppe et remonte
        - swallow=True: on exécute tout, on collecte exceptions dans les résultats

        Retour:
        - liste des retours des handlers (ou exceptions si swallow=True)
        """
        async with self._lock:
            handlers = list(self._subscribers.get(event.name, []))
            handlers += list(self._subscribers.get("*", []))

        results: List[Any] = []
        for handler in handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    results.append(await handler(event))
                else:
                    results.append(handler(event))
            except Exception as e:
                if swallow:
                    results.append(e)
                else:
                    raise
        return results
