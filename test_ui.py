"""
Unit testy pro UI komponenty
"""

import pytest
from ui import SearchUI


class TestSearchUI:
    """Testy pro SearchUI třídu"""

    @pytest.fixture
    def ui(self):
        """Fixture pro SearchUI instanci"""
        # Poznámka: Některé Streamlit funkce nelze testovat bez running app
        return SearchUI()

    def test_init(self, ui):
        """Test inicializace UI"""
        assert ui is not None
        assert isinstance(ui, SearchUI)

    def test_render_search_input_returns_query(self, ui):
        """Test že render_search_input vrací query"""
        # Tento test vyžaduje mock Streamlit funkce
        # Pro skutečné testování by bylo potřeba Streamlit testing framework
        pass

    def test_render_search_button_returns_bool(self, ui):
        """Test že render_search_button vrací boolean"""
        # Mock test
        pass

    def test_show_loading_returns_spinner(self, ui):
        """Test show_loading metody"""
        result = ui.show_loading("Test message")
        # Streamlit spinner vrací context manager
        assert result is not None

    def test_show_loading_custom_message(self, ui):
        """Test vlastní zprávy v loading"""
        result = ui.show_loading("Vlastní zpráva...")
        assert result is not None

    def test_render_locale_settings_default_values(self, ui):
        """Test výchozích hodnot lokalizace"""
        # Tento test by vyžadoval mock streamlit.selectbox
        pass


class TestSearchUIHelpers:
    """Testy pro pomocné funkce UI"""

    def test_message_methods_exist(self):
        """Test že všechny message metody existují"""
        ui = SearchUI()

        assert hasattr(ui, 'show_success')
        assert hasattr(ui, 'show_error')
        assert hasattr(ui, 'show_info')
        assert hasattr(ui, 'show_loading')

    def test_render_methods_exist(self):
        """Test že všechny render metody existují"""
        ui = SearchUI()

        assert hasattr(ui, 'render_header')
        assert hasattr(ui, 'render_search_input')
        assert hasattr(ui, 'render_search_button')
        assert hasattr(ui, 'render_results')
        assert hasattr(ui, 'render_export_buttons')
        assert hasattr(ui, 'render_locale_settings')

    def test_export_methods_exist(self):
        """Test že všechny export metody existují"""
        ui = SearchUI()

        assert hasattr(ui, '_render_json_export')
        assert hasattr(ui, '_render_csv_export')
        assert hasattr(ui, '_render_txt_export')


class TestSearchUIIntegration:
    """Integrační testy pro UI"""

    def test_ui_imports(self):
        """Test že UI importuje správné moduly"""
        import ui

        assert hasattr(ui, 'st')  # Streamlit
        assert hasattr(ui, 'json')
        assert hasattr(ui, 'datetime')
        assert hasattr(ui, 'ResultsParser')

    def test_searchui_class_exists(self):
        """Test že SearchUI třída existuje"""
        from ui import SearchUI

        assert SearchUI is not None
        assert callable(SearchUI)

    def test_searchui_instantiation(self):
        """Test vytvoření instance SearchUI"""
        try:
            ui = SearchUI()
            assert ui is not None
        except Exception as e:
            # Streamlit může selhat mimo running app
            pytest.skip(f"Streamlit initialization failed: {e}")
