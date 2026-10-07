from pathlib import Path
import sqlite3

class SeenStore:
    def __init__(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS seen (id TEXT PRIMARY KEY)")
        self.db.commit()

    def contains(self, item_id: str) -> bool:
        return self.db.execute("SELECT 1 FROM seen WHERE id=?", (item_id,)).fetchone() is not None

    def add(self, item_id: str):
        self.db.execute("INSERT OR IGNORE INTO seen(id) VALUES (?)", (item_id,))
        self.db.commit()
