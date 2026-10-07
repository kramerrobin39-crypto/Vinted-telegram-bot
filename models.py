from dataclasses import dataclass

@dataclass
class Listing:
    id: str
    title: str
    brand: str
    size: str
    price: float
    url: str
    created_at: str = ""
