"""
Point d'entrée minimal pour tester EventBus + Logger.

Usage:
- python -m kaguya.app
"""

from __future__ import annotations

import asyncio

from kaguya.core.event_bus import EventBus, Event
from kaguya.core.logger import LoggerManager


async def main() -> None:
    bus = EventBus()
    logger = LoggerManager()

    async def on_user_spoke(ev: Event):
        logger.write(
            channel="audio",
            level="INFO",
            module="audio.stt",
            event="STT_RESULT",
            payload={"text": ev.payload.get("text"), "event_id": ev.event_id},
        )
        # Exemple: transmettre au brain via event
        logger.write(
            channel="brain",
            level="INFO",
            module="brain",
            event="USER_INPUT_RECEIVED",
            payload={"text": ev.payload.get("text"), "event_id": ev.event_id},
        )

    await bus.subscribe("USER_SPOKE", on_user_spoke)

    # Simule une transcription STT
    await bus.publish(Event(name="USER_SPOKE", source="audio.stt", payload={"text": "Salut Kaguya"}))

    logger.write(channel="system", level="INFO", module="app", event="BOOT_OK", payload={})


if __name__ == "__main__":
    asyncio.run(main())
