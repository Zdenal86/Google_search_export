"""
Unit testy pro SearchService
"""

import os
from unittest.mock import MagicMock, Mock, patch

import pytest

from search_service import SearchService


class TestSearchService:
    """Testy pro SearchService třídu"""

    @pytest.fixture
    def search_service(self):
        """Fixture pro SearchService instanci

        Používá mock environment proměnné, protože SearchService
        načítá credentials z os.getenv(). Bez tohoto by test selhal,
        protože v testovacím prostředí nejsou credentials nastavené.
        """
        # Nastavíme dočasné environment proměnné pouze pro tento test
        with patch.dict(
            os.environ, {"GOOGLE_API_KEY": "test-api-key-123", "GOOGLE_CX": "test-cx-id-456"}
        ):
            return SearchService()

    def test_init(self, search_service):
        """Test inicializace služby

        Ověřuje, že:
        1. api_key byl správně načten z environment
        2. cx byl správně načten z environment
        """
        assert search_service.api_key is not None
        assert search_service.cx is not None
        assert search_service.api_key == "test-api-key-123"
        assert search_service.cx == "test-cx-id-456"

    def test_google_search_basic(self, search_service):
        """Test základního vyhledávání"""
        # Mock Google API odpověď
        mock_response = {
            "items": [
                {"title": "Test Result", "link": "https://example.com", "snippet": "Test snippet"}
            ]
        }

        # Mock build funkce pro staticmethod
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = mock_response
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            result = SearchService.google_search(
                search_service.api_key, search_service.cx, "test query", num=10
            )

            assert "items" in result
            assert len(result["items"]) == 1
            assert result["items"][0]["title"] == "Test Result"

    def test_google_search_with_locale(self, search_service):
        """Test vyhledávání s lokalizací - jazyk automaticky určuje zemi"""
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = {"items": []}
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            SearchService.google_search(
                search_service.api_key, search_service.cx, "test", num=10, language="cs"
            )

            # Ověř že byly předány správné parametry
            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]["lr"] == "lang_cs"
            assert call_args[1]["gl"] == "CZ"  # Automaticky určeno podle jazyka

    def test_google_search_num_parameter(self, search_service):
        """Test parametru num (počet výsledků)"""
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = {"items": []}
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            SearchService.google_search(
                search_service.api_key, search_service.cx, "test", num=5
            )

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]["num"] == 5

    def test_google_search_empty_query(self, search_service):
        """Test s prázdným dotazem"""
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = {"items": []}
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            result = SearchService.google_search(
                search_service.api_key, search_service.cx, "", num=10
            )

            assert isinstance(result, dict)

    def test_google_search_czech_query(self, search_service):
        """Test s českým dotazem"""
        with patch("search_service.build") as mock_build:
            mock_response = {
                "items": [{"title": "Český výsledek", "link": "http://test.cz", "snippet": "Popis"}]
            }
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = mock_response
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            result = SearchService.google_search(
                search_service.api_key, search_service.cx, "python knihy", num=10
            )

            assert result["items"][0]["title"] == "Český výsledek"

    def test_google_search_special_characters(self, search_service):
        """Test s speciálními znaky v dotazu"""
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = {"items": []}
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            special_query = "test & query <script>"
            result = SearchService.google_search(
                search_service.api_key, search_service.cx, special_query, num=10
            )

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]["q"] == special_query

    def test_google_search_max_results(self, search_service):
        """Test maximálního počtu výsledků (10)"""
        with patch("search_service.build") as mock_build:
            mock_response = {
                "items": [
                    {
                        "title": f"Result {i}",
                        "link": f"http://test{i}.com",
                        "snippet": f"Snippet {i}",
                    }
                    for i in range(1, 11)
                ]
            }
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = mock_response
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            result = SearchService.google_search(
                search_service.api_key, search_service.cx, "test", num=10
            )

            assert len(result["items"]) == 10

    def test_google_search_different_languages(self, search_service):
        """Test různých jazyků s automatickým určením země"""
        # Test mapování jazyk -> země
        language_tests = {
            "cs": "CZ",
            "en": "US",
            "sk": "SK",
            "pl": "PL",
            "de": "DE",
            "fr": "FR",
            "es": "ES",
            "it": "IT",
        }

        for lang, expected_country in language_tests.items():
            with patch("search_service.build") as mock_build:
                mock_service = Mock()
                mock_cse_instance = Mock()
                mock_list_method = Mock()

                # Mock chain: service.cse().list().execute()
                mock_list_method.execute.return_value = {"items": []}
                mock_cse_instance.list.return_value = mock_list_method
                mock_service.cse.return_value = mock_cse_instance
                mock_build.return_value = mock_service

                SearchService.google_search(
                    search_service.api_key, search_service.cx, "test", num=10, language=lang
                )

                # Ověř volání list() metody
                call_args = mock_cse_instance.list.call_args
                assert call_args[1]["lr"] == f"lang_{lang}"
                assert call_args[1]["gl"] == expected_country  # Ověř automatické určení země

    def test_google_search_unknown_language_defaults_to_us(self, search_service):
        """Test neznámého jazyka - výchozí země US"""
        with patch("search_service.build") as mock_build:
            mock_service = Mock()
            mock_cse = Mock()
            mock_list = Mock()
            mock_list.execute.return_value = {"items": []}
            mock_cse.return_value.list.return_value = mock_list
            mock_service.cse = mock_cse
            mock_build.return_value = mock_service

            SearchService.google_search(
                search_service.api_key, search_service.cx, "test", num=10, language="unknown"
            )

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]["gl"] == "US"  # Výchozí země pro neznámý jazyk
