"""
Unit testy pro ResultsParser
"""

import json

import pytest

from results_parser import ResultsParser


class TestResultsParser:
    """Testy pro ResultsParser třídu"""

    def test_parse_google_api_response_with_items(self):
        """Test parsování Google API odpovědi s items"""
        data = {
            "items": [
                {
                    "title": "Test Title 1",
                    "link": "https://example1.com",
                    "snippet": "Test snippet 1",
                },
                {
                    "title": "Test Title 2",
                    "link": "https://example2.com",
                    "snippet": "Test snippet 2",
                },
            ]
        }

        result = ResultsParser.parse_google_api_response(data)

        assert len(result) == 2
        assert result[0]["rank"] == 1
        assert result[0]["title"] == "Test Title 1"
        assert result[0]["link"] == "https://example1.com"
        assert result[0]["snippet"] == "Test snippet 1"
        assert result[1]["rank"] == 2

    def test_parse_google_api_response_with_json_string(self):
        """Test parsování Google API z JSON stringu"""
        data = json.dumps(
            {"items": [{"title": "Test", "link": "http://test.com", "snippet": "Snippet"}]}
        )

        result = ResultsParser.parse_google_api_response(data)

        assert len(result) == 1
        assert result[0]["title"] == "Test"

    def test_parse_google_api_response_with_list(self):
        """Test parsování když už jsou data v našem formátu"""
        data = [{"rank": 1, "title": "Test", "link": "http://test.com", "snippet": "Snippet"}]

        result = ResultsParser.parse_google_api_response(data)

        assert result == data

    def test_parse_google_api_response_empty(self):
        """Test parsování prázdné odpovědi"""
        result = ResultsParser.parse_google_api_response({})
        assert result == []

    def test_parse_google_api_response_missing_fields(self):
        """Test parsování s chybějícími poli"""
        data = {"items": [{"title": "Test"}]}  # Chybí link a snippet

        result = ResultsParser.parse_google_api_response(data)

        assert result[0]["title"] == "Test"
        assert result[0]["link"] == ""
        assert result[0]["snippet"] == ""

    def test_to_json_string(self):
        """Test převodu na JSON string"""
        data = {"items": [{"title": "Test", "link": "http://test.com", "snippet": "Snippet"}]}

        result = ResultsParser.to_json_string(data)

        assert isinstance(result, str)
        parsed = json.loads(result)
        assert len(parsed) == 1
        assert parsed[0]["title"] == "Test"

    def test_to_json_string_czech_characters(self):
        """Test JSON s českými znaky"""
        data = {
            "items": [
                {"title": "Český text", "link": "http://test.cz", "snippet": "Příliš žluťoučký kůň"}
            ]
        }

        result = ResultsParser.to_json_string(data)

        assert "Český text" in result
        assert "Příliš žluťoučký kůň" in result

    def test_to_csv_data(self):
        """Test převodu na CSV"""
        data = {
            "items": [
                {"title": "Test 1", "link": "http://test1.com", "snippet": "Snippet 1"},
                {"title": "Test 2", "link": "http://test2.com", "snippet": "Snippet 2"},
            ]
        }

        result = ResultsParser.to_csv_data(data)

        assert isinstance(result, str)
        assert "rank,title,link,snippet" in result
        assert "Test 1" in result
        assert "Test 2" in result

    def test_to_csv_data_without_pandas(self, monkeypatch):
        """Test CSV bez pandas"""

        def mock_import(*args, **kwargs):
            raise ImportError("No module named 'pandas'")

        monkeypatch.setattr("builtins.__import__", mock_import)

        data = {"items": [{"title": "Test", "link": "http://test.com", "snippet": "Snippet"}]}

        with pytest.raises(ImportError, match="Pandas není nainstalován"):
            ResultsParser.to_csv_data(data)

    def test_to_txt_content(self):
        """Test převodu na textový obsah"""
        data = {
            "items": [{"title": "Test Title", "link": "http://test.com", "snippet": "Test snippet"}]
        }
        query = "test query"

        result = ResultsParser.to_txt_content(data, query)

        assert isinstance(result, str)
        assert query in result
        assert "Test Title" in result
        assert "http://test.com" in result
        assert "Test snippet" in result
        assert "1." in result  # Rank číslo

    def test_to_txt_content_multiple_results(self):
        """Test TXT s více výsledky"""
        data = {
            "items": [
                {"title": f"Title {i}", "link": f"http://test{i}.com", "snippet": f"Snippet {i}"}
                for i in range(1, 6)
            ]
        }

        result = ResultsParser.to_txt_content(data, "test")

        for i in range(1, 6):
            assert f"Title {i}" in result
            assert f"{i}." in result  # Rank čísla

    def test_to_txt_content_czech_characters(self):
        """Test TXT s českými znaky"""
        data = {
            "items": [
                {"title": "Český název", "link": "http://test.cz", "snippet": "Příliš žluťoučký"}
            ]
        }

        result = ResultsParser.to_txt_content(data, "test")

        assert "Český název" in result
        assert "Příliš žluťoučký" in result

    def test_parse_large_dataset(self):
        """Test s velkým množstvím dat"""
        data = {
            "items": [
                {"title": f"Title {i}", "link": f"http://test{i}.com", "snippet": f"Snippet {i}"}
                for i in range(1, 101)  # 100 výsledků
            ]
        }

        result = ResultsParser.parse_google_api_response(data)

        assert len(result) == 100
        assert result[0]["rank"] == 1
        assert result[99]["rank"] == 100

    def test_parse_special_characters(self):
        """Test se speciálními znaky v datech"""
        data = {
            "items": [
                {
                    "title": 'Test & <script>alert("xss")</script>',
                    "link": "http://test.com?param=value&other=123",
                    "snippet": "Snippet with \"quotes\" and 'apostrophes'",
                }
            ]
        }

        result = ResultsParser.parse_google_api_response(data)

        assert result[0]["title"] == 'Test & <script>alert("xss")</script>'
        assert "&" in result[0]["link"]
