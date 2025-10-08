"""
UI komponenta pro vyhledávací aplikaci
"""

import json
from datetime import datetime

import streamlit as st

from results_parser import ResultsParser


class SearchUI:
    """Třída pro UI vyhledávací aplikace"""

    def __init__(self):
        """Inicializace UI"""
        self.setup_page()

    def setup_page(self):
        """Nastavení stránky"""
        st.set_page_config(page_title="Vyhledávač", page_icon="🔍", layout="centered")

    def render_header(self):
        """Vykreslení hlavičky"""
        st.title("🔍 Vyhledávač")
        st.write("Jednoduché vyhledávání")

    def render_search_input(self):
        """Vykreslení vyhledávacího inputu"""
        query = st.text_input("Zadejte vyhledávací dotaz:", placeholder="Např: python programming")
        return query

    def render_locale_settings(self):
        """Vykreslení nastavení lokalizace"""
        with st.expander("⚙️ Nastavení jazyka", expanded=False):
            # Mapování jazyků pro lepší UX
            language_options = {
                "Čeština (cs)": "cs",
                "English (en)": "en",
                "Slovenčina (sk)": "sk",
                "Polski (pl)": "pl",
                "Deutsch (de)": "de",
                "Français (fr)": "fr",
                "Español (es)": "es",
                "Italiano (it)": "it",
            }

            selected_display = st.selectbox(
                "Jazyk výsledků:",
                options=list(language_options.keys()),
                index=0,
                help="Vyhledávání omezí na zvolený jazyk. Země se určí automaticky.",
            )

            language = language_options[selected_display]

            return language

    def render_results_count(self):
        """Vykreslení nastavení počtu výsledků"""
        with st.expander("⚙️ Počet výsledků", expanded=False):
            count = st.number_input(
                "Zadejte počet výsledků:",
                min_value=1,
                max_value=10,
                value=5,
                help="Maximální počet výsledků, které se mají vrátit."
            )

            return count

    def render_search_button(self):
        """Vykreslení tlačítka pro vyhledání"""
        return st.button("Vyhledat", type="primary", use_container_width=True)

    def show_loading(self, message="Vyhledávám..."):
        """Zobrazení načítání"""
        return st.spinner(message)

    def show_success(self, message):
        """Zobrazení úspěšné zprávy"""
        st.success(message)

    def show_error(self, message):
        """Zobrazení chybové zprávy"""
        st.error(message)

    def show_info(self, message):
        """Zobrazení informační zprávy"""
        st.info(message)

    def render_results(self, results_json):
        """Vykreslení výsledků vyhledávání"""
        try:
            # Použij parser pro normalizaci dat
            results = ResultsParser.parse_google_api_response(results_json)

            if not results:
                self.show_info("Žádné výsledky nenalezeny")
                return

            st.divider()
            st.subheader(f"📋 Nalezeno {len(results)} výsledků")

            # Zobraz výsledky
            for result in results:
                with st.expander(
                    f"**{result.get('rank', '?')}. {result.get('title', 'Bez názvu')}**"
                ):
                    st.markdown(
                        f"**🔗 URL:** [{result.get('link', 'N/A')}]({result.get('link', '#')})"
                    )
                    st.markdown(f"**📄 Popis:** {result.get('snippet', 'Bez popisu')}")

        except Exception as e:
            self.show_error(f"Chyba při zobrazení výsledků: {e}")

    def render_export_buttons(self, results_json, query):
        """Vykreslení tlačítek pro export"""
        st.divider()
        st.subheader("📥 Export výsledků")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"vysledky_{query.replace(' ', '_')}_{timestamp}"

        col1, col2, col3 = st.columns(3)

        with col1:
            self._render_json_export(results_json, filename)

        with col2:
            self._render_csv_export(results_json, filename)

        with col3:
            self._render_txt_export(results_json, filename, query)

    def _render_json_export(self, results_json, filename):
        """Export JSON"""
        try:
            json_string = ResultsParser.to_json_string(results_json)

            st.download_button(
                label="📥 JSON",
                data=json_string,
                file_name=f"{filename}.json",
                mime="application/json",
                use_container_width=True,
            )
        except Exception as e:
            st.button("📥 JSON", disabled=True, help=f"Chyba: {e}", use_container_width=True)

    def _render_csv_export(self, results_json, filename):
        """Export CSV"""
        try:
            csv_data = ResultsParser.to_csv_data(results_json)

            st.download_button(
                label="📊 CSV",
                data=csv_data,
                file_name=f"{filename}.csv",
                mime="text/csv",
                use_container_width=True,
            )
        except ImportError:
            st.button(
                "📊 CSV", disabled=True, help="Pandas není nainstalován", use_container_width=True
            )
        except Exception as e:
            st.button("📊 CSV", disabled=True, help=f"Chyba: {e}", use_container_width=True)

    def _render_txt_export(self, results_json, filename, query):
        """Export TXT"""
        try:
            txt_content = ResultsParser.to_txt_content(results_json, query)

            st.download_button(
                label="📄 TXT",
                data=txt_content.encode("utf-8"),
                file_name=f"{filename}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        except Exception as e:
            st.button("📄 TXT", disabled=True, help=f"Chyba: {e}", use_container_width=True)
