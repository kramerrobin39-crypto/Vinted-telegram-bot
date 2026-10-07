from telegram import Bot
from models import Listing

def format_listing(item: Listing) -> str:
    return (
        "🔥 Neues Angebot\n\n"
        f"👕 {item.title}\n"
        f"🏷️ Marke: {item.brand}\n"
        f"📏 Größe: {item.size}\n"
        f"💰 Preis: {item.price:.2f} €\n"
        f"🔗 {item.url}"
    )

async def send_listing(bot: Bot, chat_id: str, item: Listing):
    await bot.send_message(chat_id=chat_id, text=format_listing(item), disable_web_page_preview=False)
