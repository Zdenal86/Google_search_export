"""
Jednoduchá vyhledávací aplikace
Objektový přístup - Streamlit + Requests + BeautifulSoup
"""

import json

import streamlit as st

from search_service import SearchService
from ui import SearchUI


def main():
    """Hlavní funkce aplikace"""

    # Inicializace komponent
    ui = SearchUI()
    search_service = SearchService()

    # Vykreslení UI
    ui.render_header()

    # Input pro vyhledávání
    query = ui.render_search_input()

    # Nastavení jazyka (země se určí automaticky)
    language = ui.render_locale_settings()

    # Nastavení počtu výsledků
    results_count = ui.render_results_count()

    # Tlačítko vyhledat
    if ui.render_search_button():
        if query and query.strip():
            with ui.show_loading():
                # Vyhledání s lokalizací (staticmethod s cache)
                results_dict = SearchService.google_search(
                    search_service.api_key,
                    search_service.cx,
                    query,
                    results_count,
                    language=language
                )

                # Uložení do session state
                st.session_state.results_json = json.dumps(
                    results_dict, ensure_ascii=False, indent=2
                )
                st.session_state.query = query

            # Zobrazení úspěšné zprávy
            ui.show_success(f"✅ Vyhledávání dokončeno")

        else:
            ui.show_error("⚠️ Zadejte vyhledávací dotaz!")

    # Zobrazení výsledků (pokud existují v session_state) a export tlačítka (pokud existují výsledky)
    if hasattr(st.session_state, "results_json") and st.session_state.results_json:
        ui.render_results(st.session_state.results_json)
        ui.render_export_buttons(st.session_state.results_json, st.session_state.query)


if __name__ == "__main__":
    main()
