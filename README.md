# Vinted → Telegram Angebots-Bot

Konfiguration für:
- Preis 0–25 €
- Größen S, M, L
- Marken Nike, Adidas, Ralph Lauren, Lacoste, Tommy Hilfiger, Levi's
- Kategorien: T-Shirt, Polo, Hoodie, Pullover, Hose, Jacke
- Ausschluss: Schuhe, Socken, Accessoires
- nur neue Treffer
- neueste Angebote zuerst

## Wichtiger Hinweis
Vinted hat keine allgemeine öffentliche API für die Suche nach fremden Marketplace-Angeboten. Dieses Projekt ist deshalb als sauber getrennte Bot-Struktur vorbereitet: Der `VintedSource` erwartet einen von dir autorisierten/zulässigen Datenzugang. Bitte keine Zugangsdaten oder Session-Cookies in die ZIP eintragen und Vinteds Nutzungsbedingungen beachten.

## Einrichtung
1. Python 3.11+ installieren.
2. `pip install -r requirements.txt`
3. `.env.example` nach `.env` kopieren.
4. Bei Telegram mit @BotFather einen Bot erstellen und `TELEGRAM_BOT_TOKEN` eintragen.
5. `TELEGRAM_CHAT_ID` eintragen.
6. Einen zulässigen Vinted-Datenfeed/zugelassenen Zugang in `src/vinted_source.py` implementieren.
7. `python main.py` starten.

Der Bot speichert bereits gemeldete Listing-IDs in SQLite und sendet jedes Listing nur einmal.
