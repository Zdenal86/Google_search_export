"""
Vyhledávací služba
"""

import os
import streamlit as st
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

    # Statická metoda kvůli cachování
    @staticmethod
    @st.cache_data(ttl=3600)
    def google_search(api_key, cx, query, num, language="cs"):
        """
        Provede vyhledávání pomocí Google Custom Search API

        Args:
            api_key: Google Custom Search API klíč
            cx: Custom Search Engine ID
            query: Vyhledávací dotaz
            num: Počet výsledků (max 10)
            language: Jazyk výsledků (cs, en, sk, pl, de, fr, es, it)
                     Země pro geolokalizaci se automaticky určí podle jazyka

        Returns:
            dict: Google API odpověď
        """
         # Tato zpráva se vypíše JEN když se volá API (ne z cache)
        print(f"🔴 API CALL: {query}, {num}, {language}")  # ← Do konzole
        # Build service v rámci cachovatelné funkce
        service = build("customsearch", "v1", developerKey=api_key)

        # Automaticky určí zemi podle zvoleného jazyka
        country = SearchService.LANGUAGE_COUNTRY_MAP.get(language, "US")

        res = (
            service.cse()
            .list(
                q=query,
                cx=cx,
                num=num,
                lr=f"lang_{language}",  # Language restrict - omezí výsledky na daný jazyk
                gl=country,  # Geolocation - automaticky podle jazyka
            )
            .execute()
        )
        return res
