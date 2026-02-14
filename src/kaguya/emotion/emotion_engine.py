"""
EmotionEngine minimal de Kaguya IA.

Responsabilités :
- Maintenir l'état émotionnel immédiat
- Évaluer un stimulus simple
- Logger les mises à jour émotionnelles
- Émettre un événement EMOTION_UPDATED

Impacte :
- EventBus
- Logger
"""

from __future__ import annotations

from typing import Dict, Any
from kaguya.core.event_bus import Event, EventBus
from kaguya.core.logger import LoggerManager
from .immediate_state import ImmediateState


class EmotionEngine:
    """
    Version minimale fonctionnelle.

    Fonctionnement :
    - S'abonne à USER_SPOKE
    - Analyse stimulus basique
    - Ajuste irritation/trust
    - Log l'évolution
    - Émet EMOTION_UPDATED
    """

    def __init__(self, bus: EventBus, logger: LoggerManager) -> None:
        self.bus = bus
        self.logger = logger
        self.state = ImmediateState()

    async def start(self) -> None:
        await self.bus.subscribe("USER_SPOKE", self.on_user_spoke)

    async def on_user_spoke(self, event: Event) -> None:
        text: str = event.payload.get("text", "").lower()

        self.evaluate_stimulus(text)

        self.logger.write(
            channel="emotion",
            level="EMOTION_UPDATE",
            module="emotion",
            event="STATE_UPDATED",
            payload=self.state.snapshot(),
        )

        await self.bus.publish(
            Event(
                name="EMOTION_UPDATED",
                source="emotion",
                payload=self.state.snapshot(),
            )
        )

    def evaluate_stimulus(self, text: str) -> None:
        """
        Analyse extrêmement simple :

        - Si texte contient 'ordre' ou impératif fort → irritation +0.1
        - Sinon → trust +0.02
        """

        if "!" in text:
            self.state.irritation += 0.1
        else:
            self.state.trust += 0.02

        self.state.clamp()
