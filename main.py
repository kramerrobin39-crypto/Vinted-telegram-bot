import asyncio
from telegram import Bot
from config import Config
from filters import matches
from storage import SeenStore
from src.vinted_source import VintedSource
from telegram_bot import send_listing

async def run():
    cfg = Config()
    if not cfg.telegram_token or not cfg.chat_id:
        raise RuntimeError("TELEGRAM_BOT_TOKEN und TELEGRAM_CHAT_ID müssen in .env gesetzt werden.")

    bot = Bot(cfg.telegram_token)
    store = SeenStore(cfg.database_path)
    source = VintedSource()

    while True:
        try:
            items = await source.latest()
            for item in items:  # Quelle liefert newest-first
                if matches(item) and not store.contains(item.id):
                    await send_listing(bot, cfg.chat_id, item)
                    store.add(item.id)
        except Exception as exc:
            print(f"[ERROR] {exc}")
        await asyncio.sleep(cfg.poll_seconds)

if __name__ == "__main__":
    asyncio.run(run())
