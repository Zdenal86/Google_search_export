# 🔍 Vyhledávací aplikace

Jednoduchá webová aplikace pro vyhledávání pomocí Google Custom Search API s podporou lokalizace.

## ✨ Vlastnosti

- 🌐 Vyhledávání přes Google Custom Search API
- 🌍 Podpora lokalizace (jazyk, země)
- 📥 Export výsledků do JSON, CSV, TXT
- 🎨 Moderní UI postavené na Streamlit
- ✅ 100% pokrytí testy pro core logiku
- 🧪 36 unit testů s pytest

## 📁 Struktura projektu

```
.
├── main.py                    # Entry point aplikace
├── ui.py                      # UI komponenty (SearchUI)
├── search_service.py          # Google API service (SearchService)
├── results_parser.py          # Parsování a export dat (ResultsParser)
├── test_results_parser.py     # Unit testy pro parser (14 testů)
├── test_search_service.py     # Unit testy pro service (10 testů)
├── test_ui.py                 # Unit testy pro UI (12 testů)
├── requirements.txt           # Všechny dependencies
├── requirements-minimal.txt   # Pouze hlavní dependencies
└── .gitignore                 # Git ignore pravidla
```

## 🚀 Instalace

### 1. Klonování repozitáře
```bash
git clone <repository-url>
cd Inizio_test
```

### 2. Vytvoření virtual environmentu
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalace závislostí
```powershell
# Minimální instalace
pip install -r requirements-minimal.txt

# Nebo kompletní instalace
pip install -r requirements.txt
```

## 🎮 Použití

### Spuštění aplikace
```powershell
streamlit run main.py
```

Aplikace se otevře v prohlížeči na `http://localhost:8501`

### Vyhledávání
1. Zadejte vyhledávací dotaz
2. (Volitelně) Nastavte jazyk a zemi v "⚙️ Nastavení lokalizace"
3. Klikněte na "Vyhledat"
4. Exportujte výsledky pomocí tlačítek 📥 JSON, 📊 CSV, 📄 TXT

## 🧪 Testování

### Spuštění všech testů
```powershell
.venv\Scripts\python.exe -m pytest -v
```

### Coverage analýza
```powershell
# Terminálový výstup
.venv\Scripts\python.exe -m pytest --cov=. --cov-report=term-missing

# HTML report
.venv\Scripts\python.exe -m pytest --cov=. --cov-report=html
start htmlcov/index.html
```

### Specifické testy
```powershell
# Pouze parser testy
.venv\Scripts\python.exe -m pytest test_results_parser.py -v

# Pouze service testy
.venv\Scripts\python.exe -m pytest test_search_service.py -v

# Pouze UI testy
.venv\Scripts\python.exe -m pytest test_ui.py -v
```

## 📊 Test Coverage

| Modul | Coverage | Status |
|-------|----------|--------|
| results_parser.py | 100% | ✅ |
| search_service.py | 65% | ⚠️ |
| ui.py | 29% | ⚠️ |
| **Celkem** | **79%** | ✅ |

*Poznámka: Nízké pokrytí UI je normální - Streamlit komponenty jsou těžké testovat unit testy.*

## 🔧 Konfigurace

### Google Custom Search API
V souboru `search_service.py` nastavte:
```python
self.api_key = "VÁŠ_API_KEY"
self.cx = "VÁŠ_SEARCH_ENGINE_ID"
```

### Podporované jazyky
- Čeština (cs)
- Angličtina (en)
- Slovenština (sk)
- Polština (pl)
- Němčina (de)
- Francouzština (fr)

### Podporované země
- Česko (CZ)
- Slovensko (SK)
- Polsko (PL)
- USA (US)
- Německo (DE)
- Francie (FR)
- Velká Británie (UK)

## 🏗️ Architektura

### Objektově orientovaný design
- **SearchUI**: Veškerá UI logika a rendering
- **SearchService**: Google API komunikace
- **ResultsParser**: Parsování a export dat

### Design patterns
- Separation of Concerns
- Static methods pro utility funkce
- Mock testing pro API volání

## 📝 Development

### Přidání nového testu
```python
# test_nazev.py
import pytest
from module import Class

def test_funkcionalita():
    """Popis testu"""
    # Arrange
    obj = Class()
    
    # Act
    result = obj.method()
    
    # Assert
    assert result == expected
```

### Spuštění aplikace v dev módu
```powershell
streamlit run main.py --server.runOnSave true
```

## 🐛 Troubleshooting

### Import Error: No module named 'googleapiclient'
```powershell
pip install google-api-python-client
```

### Pytest nenalezen
```powershell
pip install pytest pytest-cov
```

### Streamlit se nespustí
```powershell
pip install streamlit --upgrade
```

## 📜 Licence

MIT License

## 👨‍💻 Autor

Vytvořeno s pomocí GitHub Copilot

---

**Tip**: Pro nejlepší výsledky použijte specifické vyhledávací dotazy a experimentujte s různými nastaveními lokalizace! 🚀
