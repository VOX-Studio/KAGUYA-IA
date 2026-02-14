"""
Logger central structuré (JSON) pour Kaguya IA.

Objectifs:
- Unifier les logs de tous les modules.
- Permettre debug et audit ("bug vs comportement volontaire").
- Rotation simple par taille.
- Séparation par "channel" (emotion, audio, actions, brain, memory, system, performance).

Fichiers/Modules impactés:
- Tous les modules doivent écrire via LoggerManager, pas via print().
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class LogRecord:
    """
    Représente un enregistrement de log structuré.
    """
    timestamp: str
    ts_ms: int
    level: str
    module: str
    event: str
    payload: Dict[str, Any]


class LoggerManager:
    """
    Logger central.

    - log_dir: dossier de sortie logs/
    - rotation_bytes: taille max d'un fichier avant rotation .1, .2, etc.
    - channels: fichiers séparés (ex: emotion.log, audio.log...)

    Format:
    Une ligne = un JSON.
    """

    def __init__(self, log_dir: str = "logs", rotation_bytes: int = 5_000_000) -> None:
        self.log_dir = log_dir
        self.rotation_bytes = rotation_bytes
        os.makedirs(self.log_dir, exist_ok=True)

    def _now(self) -> LogRecord:
        ts_ms = int(time.time() * 1000)
        # ISO-lite lisible
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(ts_ms / 1000))
        return LogRecord(timestamp=timestamp, ts_ms=ts_ms, level="INFO", module="system", event="noop", payload={})

    def _file_path(self, channel: str) -> str:
        return os.path.join(self.log_dir, f"{channel}.log")

    def _rotate_if_needed(self, path: str) -> None:
        if not os.path.exists(path):
            return
        if os.path.getsize(path) < self.rotation_bytes:
            return

        # Rotation simple: .1, .2, .3 (jusqu'à 5)
        for i in range(5, 0, -1):
            src = f"{path}.{i}"
            dst = f"{path}.{i+1}"
            if os.path.exists(src):
                os.replace(src, dst)
        os.replace(path, f"{path}.1")

    def write(
        self,
        *,
        channel: str,
        level: str,
        module: str,
        event: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Écrit un log structuré.

        channel: ex "emotion", "audio", "actions", "brain", "memory", "system", "performance"
        level: DEBUG/INFO/WARNING/ERROR/CRITICAL + DECISION/EMOTION_UPDATE/REFLECTION/BASELINE_SHIFT/AUTONOMOUS_ACTION
        """
        payload = payload or {}
        base = self._now()
        record = LogRecord(
            timestamp=base.timestamp,
            ts_ms=base.ts_ms,
            level=level,
            module=module,
            event=event,
            payload=payload,
        )

        path = self._file_path(channel)
        self._rotate_if_needed(path)

        line = json.dumps(record.__dict__, ensure_ascii=False)
        with open(path, "a", encoding="utf-8") as f:
            f.write(line + "\n")
