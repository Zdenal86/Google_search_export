"""
Unit testy pro SearchService
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from search_service import SearchService


class TestSearchService:
    """Testy pro SearchService třídu"""

    @pytest.fixture
    def search_service(self):
        """Fixture pro SearchService instanci"""
        return SearchService()

    def test_init(self, search_service):
        """Test inicializace služby"""
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
        """Test vyhledávání s lokalizací"""
        with patch.object(search_service.service, 'cse') as mock_cse:
            mock_list = Mock()
            mock_execute = Mock(return_value={'items': []})
            mock_list.execute = mock_execute
            mock_cse.return_value.list.return_value = mock_list

            search_service.google_search("test", language='cs', country='CZ')

            # Ověř že byly předány správné parametry
            call_args = mock_cse.return_value.list.call_args
            assert call_args[1]['lr'] == 'lang_cs'
            assert call_args[1]['gl'] == 'CZ'
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
        """Test různých jazyků"""
        languages = ['cs', 'en', 'sk', 'pl', 'de']

        for lang in languages:
            with patch.object(search_service.service, 'cse') as mock_cse:
                mock_list = Mock()
                mock_execute = Mock(return_value={'items': []})
                mock_list.execute = mock_execute
                mock_cse.return_value.list.return_value = mock_list

                search_service.google_search("test", language=lang)

                call_args = mock_cse.return_value.list.call_args
                assert call_args[1]['lr'] == f'lang_{lang}'
                assert call_args[1]['hl'] == lang

    def test_google_search_different_countries(self, search_service):
        """Test různých zemí"""
        countries = ['CZ', 'SK', 'US', 'DE', 'FR']

        for country in countries:
            with patch.object(search_service.service, 'cse') as mock_cse:
                mock_list = Mock()
                mock_execute = Mock(return_value={'items': []})
                mock_list.execute = mock_execute
                mock_cse.return_value.list.return_value = mock_list

                search_service.google_search("test", country=country)

                call_args = mock_cse.return_value.list.call_args
                assert call_args[1]['gl'] == country
