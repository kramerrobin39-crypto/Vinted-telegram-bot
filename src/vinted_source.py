# Adapter für einen zulässigen Vinted-Datenzugang.
#
# Vinted bietet keine allgemeine öffentliche API für die Suche nach
# fremden Marketplace-Angeboten. Daher wird hier absichtlich kein
# inoffizieller Scraper eingebaut.
#
# Implementiere `latest()` mit einem von dir autorisierten/zulässigen
# Feed oder einer ausdrücklich erlaubten Schnittstelle.
#
# Erwartung: Rückgabe ist eine Liste von models.Listing, bereits nach
# newest-first sortiert.

class VintedSource:
    async def latest(self):
        return []
