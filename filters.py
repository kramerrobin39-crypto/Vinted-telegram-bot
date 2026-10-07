from config import BRANDS, SIZES, ALLOWED_TERMS, BLOCKED_TERMS
from models import Listing

def matches(item: Listing) -> bool:
    if not (0 <= item.price <= 25):
        return False

    brand = item.brand.lower().strip()
    title = item.title.lower()

    if brand not in BRANDS and not any(b in title for b in BRANDS):
        return False

    if item.size.lower().strip() not in SIZES:
        return False

    if not any(term in title for term in ALLOWED_TERMS):
        return False

    if any(term in title for term in BLOCKED_TERMS):
        return False

    return True
