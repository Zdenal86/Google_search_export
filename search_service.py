"""
Vyhledávací služba
"""

import json
import os

from googleapiclient.discovery import build


class SearchService:
    """Třída pro vyhledávání"""

    # Mapování jazyka na výchozí zemi pro geolokalizaci
    LANGUAGE_COUNTRY_MAP = {
        "cs": "CZ",  # Čeština -> Česká republika
        "sk": "SK",  # Slovenština -> Slovensko
        "pl": "PL",  # Polština -> Polsko
        "de": "DE",  # Němčina -> Německo
        "fr": "FR",  # Francouzština -> Francie
        "en": "US",  # Angličtina -> USA
        "es": "ES",  # Španělština -> Španělsko
        "it": "IT",  # Italština -> Itálie
    }

    def __init__(self):
        """Inicializace služby

        API klíč a CX se načítají z environment proměnných:
        - GOOGLE_API_KEY: Google Custom Search API klíč
        - GOOGLE_CX: Custom Search Engine ID

        Pro lokální vývoj lze použít fallback hodnoty nebo .env soubor
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cx = os.getenv("GOOGLE_CX")
        self.service = build("customsearch", "v1", developerKey=self.api_key)

    def google_search(self, query, num, language="cs"):
        """
        Provede vyhledávání pomocí Google Custom Search API

        Args:
            query: Vyhledávací dotaz
            num: Počet výsledků (max 10)
            language: Jazyk výsledků (cs, en, sk, pl, de, fr, es, it)
                     Země pro geolokalizaci se automaticky určí podle jazyka

        Returns:
            dict: Google API odpověď
        """
        # Automaticky určí zemi podle zvoleného jazyka
        country = self.LANGUAGE_COUNTRY_MAP.get(language, "US")

        res = (
            self.service.cse()
            .list(
                q=query,
                cx=self.cx,
                num=num,
                lr=f"lang_{language}",  # Language restrict - omezí výsledky na daný jazyk
                gl=country,  # Geolocation - automaticky podle jazyka
            )
            .execute()
        )
        return res
