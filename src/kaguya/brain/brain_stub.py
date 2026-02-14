"""
BrainStub minimal pour permettre communication.

Responsabilités :
- Écouter USER_SPOKE
- Générer réponse simple
- Intégrer état émotionnel courant
- Publier KAGUYA_RESPONSE

Impacte :
- EventBus
- Logger
- EmotionEngine (via EMOTION_UPDATED)
"""

from __future__ import annotations

from kaguya.core.event_bus import Event, EventBus
from kaguya.core.logger import LoggerManager


class BrainStub:
    """
    Brain temporaire avant intégration LLM.

    Fonctionnement :
    - Récupère EMOTION_UPDATED pour snapshot
    - Répond à USER_SPOKE
    """

    def __init__(self, bus: EventBus, logger: LoggerManager) -> None:
        self.bus = bus
        self.logger = logger
        self.current_emotion = {}

    async def start(self) -> None:
        await self.bus.subscribe("USER_SPOKE", self.on_user_spoke)
        await self.bus.subscribe("EMOTION_UPDATED", self.on_emotion_updated)

    async def on_emotion_updated(self, event: Event) -> None:
        self.current_emotion = event.payload

    async def on_user_spoke(self, event: Event) -> None:
        user_text = event.payload.get("text", "")
        response = self.generate_response(user_text)

        self.logger.write(
            channel="brain",
            level="INFO",
            module="brain",
            event="RESPONSE_GENERATED",
            payload={"response": response}
        )

        await self.bus.publish(
            Event(
                name="KAGUYA_RESPONSE",
                source="brain",
                payload={"text": response}
            )
        )

    def generate_response(self, user_text: str) -> str:
        """
        Réponse simple influencée par irritation.
        """
        irritation = self.current_emotion.get("irritation", 0)

        if irritation > 0.5:
            return "Tu pourrais parler un peu plus calmement, non ?"
        return f"Je t'écoute. Tu as dit : {user_text}"
