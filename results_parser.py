"""
Parser pro Google API odpovědi
"""


class ResultsParser:
    """Třída pro parsování výsledků z různých zdrojů"""

    @staticmethod
    def parse_google_api_response(results):
        """
        Parsuje Google Custom Search API odpověď

        Args:
            results: dict nebo str s API odpovědí

        Returns:
            list: Normalizovaná data ve formátu [{'rank', 'title', 'link', 'snippet'}]
        """
        import json

        # Kontrola typu
        if isinstance(results, str):
            results = json.loads(results)

        # Parsování Google API struktury
        if "items" in results:
            items = results["items"]
            data = []
            for i, item in enumerate(items, 1):
                data.append(
                    {
                        "rank": i,
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "snippet": item.get("snippet", ""),
                    }
                )
            return data

        # Fallback - data už jsou v našem formátu
        elif isinstance(results, list):
            return results

        # Fallback - prázdná odpověď
        return []

    @staticmethod
    def to_json_string(results):
        """
        Převede parsovaná data na JSON string

        Args:
            results: list nebo dict s daty

        Returns:
            str: JSON string
        """
        import json

        parsed = ResultsParser.parse_google_api_response(results)
        return json.dumps(parsed, ensure_ascii=False, indent=2)

    @staticmethod
    def to_csv_data(results):
        """
        Převede parsovaná data na CSV

        Args:
            results: list nebo dict s daty

        Returns:
            str: CSV string
        """
        try:
            import pandas as pd

            parsed = ResultsParser.parse_google_api_response(results)
            df = pd.DataFrame(parsed)
            return df.to_csv(index=False, encoding="utf-8")
        except ImportError:
            raise ImportError("Pandas není nainstalován")

    @staticmethod
    def to_txt_content(results, query):
        """
        Převede parsovaná data na textový obsah

        Args:
            results: list nebo dict s daty
            query: vyhledávací dotaz

        Returns:
            str: Textový obsah
        """
        from datetime import datetime

        parsed = ResultsParser.parse_google_api_response(results)

        txt_content = f"Výsledky vyhledávání: {query}\n"
        txt_content += f"Čas: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        txt_content += "=" * 60 + "\n\n"

        for result in parsed:
            txt_content += f"{result.get('rank', '?')}. {result.get('title', 'Bez názvu')}\n"
            txt_content += f"   URL: {result.get('link', 'N/A')}\n"
            txt_content += f"   {result.get('snippet', 'Bez popisu')}\n\n"

        return txt_content
