"""
Unit testy pro SearchService
"""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock
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
        with patch.dict(os.environ, {
            'GOOGLE_API_KEY': 'test-api-key-123',
            'GOOGLE_CX': 'test-cx-id-456'
        }):
            return SearchService()

    def test_init(self, search_service):
        """Test inicializace služby

        Ověřuje, že:
        1. api_key byl správně načten z environment
        2. cx byl správně načten z environment
        3. Google API service byl úspěšně inicializován
        """
        assert search_service.api_key is not None
        assert search_service.cx is not None
        assert search_service.service is not None

    def test_google_search_basic(self, search_service):
        """Test základního vyhledávání"""
        # Mock Google API odpověď
        mock_response = {
            'items': [
                {
                    'title': 'Test Result',
                    'link': 'https://example.com',
                    'snippet': 'Test snippet'
                }
            ]
        }

        # Nastavení mocku
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value=mock_response)
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            result = search_service.google_search("test query")

            assert 'items' in result
            assert len(result['items']) == 1
            assert result['items'][0]['title'] == 'Test Result'

    def test_google_search_with_locale(self, search_service):
        """Test vyhledávání s lokalizací - jazyk automaticky určuje zemi"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            search_service.google_search("test", language='cs')

            # Ověř že byly předány správné parametry
            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]['lr'] == 'lang_cs'
            assert call_args[1]['gl'] == 'CZ'  # Automaticky určeno podle jazyka
            assert call_args[1]['hl'] == 'cs'

    def test_google_search_num_parameter(self, search_service):
        """Test parametru num (počet výsledků)"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            search_service.google_search("test", num=5)

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]['num'] == 5

    def test_google_search_empty_query(self, search_service):
        """Test s prázdným dotazem"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            result = search_service.google_search("")

            assert isinstance(result, dict)

    def test_google_search_czech_query(self, search_service):
        """Test s českým dotazem"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_response = {
                'items': [
                    {'title': 'Český výsledek', 'link': 'http://test.cz', 'snippet': 'Popis'}
                ]
            }
            mock_list = Mock()
            mock_execute = Mock(return_value=mock_response)
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            result = search_service.google_search("python knihy")

            assert result['items'][0]['title'] == 'Český výsledek'

    def test_google_search_special_characters(self, search_service):
        """Test s speciálními znaky v dotazu"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            special_query = "test & query <script>"
            result = search_service.google_search(special_query)

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]['q'] == special_query

    def test_google_search_max_results(self, search_service):
        """Test maximálního počtu výsledků (10)"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_response = {
                'items': [
                    {'title': f'Result {i}', 'link': f'http://test{i}.com', 'snippet': f'Snippet {i}'}
                    for i in range(1, 11)
                ]
            }
            mock_list = Mock()
            mock_execute = Mock(return_value=mock_response)
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            result = search_service.google_search("test", num=10)

            assert len(result['items']) == 10

    def test_google_search_different_languages(self, search_service):
        """Test různých jazyků s automatickým určením země"""
        # Test mapování jazyk -> země
        language_tests = {
            'cs': 'CZ',
            'en': 'US',
            'sk': 'SK',
            'pl': 'PL',
            'de': 'DE',
            'fr': 'FR',
            'es': 'ES',
            'it': 'IT',
        }

        for lang, expected_country in language_tests.items():
            with patch.object(search_service.service, 'cse') as mock_cse:
                mock_list = Mock()
                mock_execute = Mock(return_value={'items': []})
                mock_list.execute = mock_execute
                mock_cse.return_value.list.return_value = mock_list

                search_service.google_search("test", language=lang)

                call_args = mock_cse.return_value.list.call_args
                assert call_args[1]['lr'] == f'lang_{lang}'
                assert call_args[1]['hl'] == lang
                assert call_args[1]['gl'] == expected_country  # Ověř automatické určení země

    def test_google_search_unknown_language_defaults_to_us(self, search_service):
        """Test neznámého jazyka - výchozí země US"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            search_service.google_search("test", language='unknown')

            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]['gl'] == 'US'  # Výchozí země pro neznámý jazyk
