"""
Point d'entrée principal – Boucle interactive minimale.
"""

from __future__ import annotations

import asyncio

from kaguya.core.event_bus import EventBus, Event
from kaguya.core.logger import LoggerManager
from kaguya.emotion import EmotionEngine
from kaguya.brain import BrainStub


async def main() -> None:
    print("Kaguya boot...")

    bus = EventBus()
    logger = LoggerManager()

    emotion_engine = EmotionEngine(bus, logger)
    brain = BrainStub(bus, logger)

    await emotion_engine.start()
    await brain.start()

    async def console_output(event: Event):
        print(f"Kaguya : {event.payload.get('text')}")

    await bus.subscribe("KAGUYA_RESPONSE", console_output)

    print("Tu peux parler à Kaguya (écris 'exit' pour quitter)\n")

    while True:
        user_input = input("Toi : ")

        if user_input.lower() == "exit":
            break

        await bus.publish(
            Event(
                name="USER_SPOKE",
                source="console",
                payload={"text": user_input}
            )
        )

    print("Arrêt de Kaguya.")


if __name__ == "__main__":
    asyncio.run(main())
