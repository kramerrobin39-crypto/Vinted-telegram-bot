from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    telegram_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")
    poll_seconds: int = int(os.getenv("POLL_SECONDS", "60"))
    database_path: str = os.getenv("DATABASE_PATH", "data/seen.sqlite3")

BRANDS = {
    "nike", "adidas", "ralph lauren", "lacoste", "tommy hilfiger", "levis", "levi's"
}
SIZES = {"s", "m", "l"}
ALLOWED_TERMS = {
    "t-shirt", "tshirt", "t shirt", "polo", "hoodie",
    "hoody", "pullover", "sweater", "hose", "pants",
    "jeans", "trousers", "jacke", "jacket"
}
BLOCKED_TERMS = {
    "schuhe", "shoe", "shoes", "socken", "socks",
    "accessoire", "accessoires", "accessory", "bag", "tasche",
    "cap", "mütze", "gürtel", "belt", "scarf", "schal"
}
