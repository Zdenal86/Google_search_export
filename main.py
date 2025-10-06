"""
Jednoduchá vyhledávací aplikace
Objektový přístup - Streamlit + Requests + BeautifulSoup
"""

import streamlit as st
from ui import SearchUI
from search_service import SearchService
import json


def main():
    """Hlavní funkce aplikace"""

    # Inicializace komponent
    ui = SearchUI()
    search_service = SearchService()

    # Vykreslení UI
    ui.render_header()

    # Input pro vyhledávání
    query = ui.render_search_input()

    # Nastavení lokalizace
    language, country = ui.render_locale_settings()

    # Tlačítko vyhledat
    if ui.render_search_button():
        if query and query.strip():
            with ui.show_loading():
                # Vyhledání s lokalizací
                results_dict = search_service.google_search(
                    query,
                    language=language,
                    country=country
                )

                # Uložení do session state
                st.session_state.results_json = json.dumps(results_dict, ensure_ascii=False, indent=2)
                st.session_state.query = query

            # Zobrazení výsledků
            ui.show_success(f"✅ Vyhledávání dokončeno")
            ui.render_results(results_dict)

        else:
            ui.show_error("⚠️ Zadejte vyhledávací dotaz!")

    # Export tlačítka (pokud existují výsledky)
    if hasattr(st.session_state, 'results_json') and st.session_state.results_json:
        ui.render_export_buttons(st.session_state.results_json, st.session_state.query)



if __name__ == "__main__":
    main()


