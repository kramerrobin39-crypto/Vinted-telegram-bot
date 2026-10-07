import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    telegram_token: str = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id: str = os.environ.get("TELEGRAM_CHAT_ID", "")
    poll_seconds: int = int(os.environ.get("POLL_SECONDS", "60"))
    database_path: str = os.environ.get("DATABASE_PATH", "data/seen.sqlite3")


BRANDS = {
    "nike", "adidas", "ralph lauren", "lacoste",
    "tommy hilfiger", "levis", "levi's"
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
