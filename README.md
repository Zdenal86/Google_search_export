# 🔍 Vyhledávací aplikace

[![Tests](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/tests.yml/badge.svg)](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/tests.yml)
[![Quick CI](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/quick-ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/quick-ci.yml)
[![Code Quality](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/code-quality.yml/badge.svg)](https://github.com/YOUR_USERNAME/Google_search_export/actions/workflows/code-quality.yml)
[![codecov](https://codecov.io/gh/YOUR_USERNAME/Google_search_export/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/Google_search_export)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Jednoduchá webová aplikace pro vyhledávání pomocí Google Custom Search API s podporou lokalizace.

## ✨ Vlastnosti

- 🌐 Vyhledávání přes Google Custom Search API
- 🌍 Inteligentní lokalizace (automatické určení země podle jazyka)
- 📥 Export výsledků do JSON, CSV, TXT
- 🎨 Moderní UI postavené na Streamlit
- ✅ 100% pokrytí testy pro business logiku (parser + service)
- 🧪 36 unit testů s pytest (35 passing)

## 📁 Struktura projektu

```
.
├── main.py                    # Entry point aplikace
├── ui.py                      # UI komponenty (SearchUI)
├── search_service.py          # Google API service (SearchService)
├── results_parser.py          # Parsování a export dat (ResultsParser)
├── test_results_parser.py     # Unit testy pro parser (14 testů, 100% coverage)
├── test_search_service.py     # Unit testy pro service (10 testů, 100% coverage)
├── test_ui.py                 # Unit testy pro UI (12 testů, 30% coverage)
├── requirements.txt           # Všechny dependencies
├── requirements-minimal.txt   # Pouze hlavní dependencies
└── .gitignore                 # Git ignore pravidla
```

## 🚀 Instalace

### 1. Klonování repozitáře

```bash
git clone <repository-url>
cd Google_search_export
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

### 4. Konfigurace API credentials (volitelné)

Aplikace má fallback hodnoty pro rychlý start. Pro produkci nastavte vlastní credentials:

#### Pro lokální vývoj - vytvoř `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "váš-google-api-klíč"
GOOGLE_CX = "váš-cx-id"
```

#### Nebo použij environment proměnné:

```powershell
$env:GOOGLE_API_KEY = "váš-api-klíč"
$env:GOOGLE_CX = "váš-cx"
```

> 📚 Podrobný návod na získání credentials viz [DEPLOYMENT.md](DEPLOYMENT.md)

## 🎮 Použití

### Spuštění aplikace

```powershell
streamlit run main.py
```

Aplikace se otevře v prohlížeči na `http://localhost:8501`

### Vyhledávání

1. Zadejte vyhledávací dotaz
2. (Volitelně) Zvolte jazyk v "⚙️ Nastavení jazyka" - země se určí automaticky
3. Klikněte na "Vyhledat"
4. Exportujte výsledky pomocí tlačítek 📥 JSON, 📊 CSV, 📄 TXT

### Podporované jazyky

Aplikace podporuje 8 jazyků s automatickým určením odpovídající země:

- 🇨🇿 Čeština (cs) → Česká republika
- 🇬🇧 English (en) → USA
- 🇸🇰 Slovenčina (sk) → Slovensko
- 🇵🇱 Polski (pl) → Polsko
- 🇩🇪 Deutsch (de) → Německo
- 🇫🇷 Français (fr) → Francie
- 🇪🇸 Español (es) → Španělsko
- 🇮🇹 Italiano (it) → Itálie

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

| Modul             | Coverage | Testy  | Status |
| ----------------- | -------- | ------ | ------ |
| results_parser.py | 100%     | 14     | ✅     |
| search_service.py | 100%     | 10     | ✅     |
| ui.py             | 30%      | 12     | ⚠️     |
| **Celkem**        | **51%**  | **36** | ✅     |

_Poznámka: Nízké pokrytí UI je normální - Streamlit komponenty jsou těžké testovat unit testy._

## 🔄 CI/CD (GitHub Actions)

Projekt má nastavené tři GitHub Actions workflows:

### 1. **Tests** (`.github/workflows/tests.yml`)

- Spouští se při push/PR do `main` nebo `develop`
- Testuje na **Ubuntu, Windows, macOS**
- Testuje Python verze: **3.10, 3.11, 3.12, 3.13**
- Generuje coverage report
- Nahrává do **Codecov**
- Ukládá HTML coverage jako artifact

### 2. **Quick CI** (`.github/workflows/quick-ci.yml`)

- Rychlé testy na Ubuntu + Python 3.11
- Kontroluje coverage threshold (min. 70%)
- Ideální pro rychlou zpětnou vazbu

### 3. **Code Quality** (`.github/workflows/code-quality.yml`)

- **Linting**: flake8, pylint
- **Formatting**: black, isort
- **Type checking**: mypy
- **Security**: bandit, safety
- Výsledky jako artifacts

### Lokální spuštění CI kontrol

```powershell
# Formátování
black --check .
isort --check-only .

# Linting
flake8 .
pylint **/*.py

# Type checking
mypy . --ignore-missing-imports

# Security check
bandit -r .
safety check
```

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

## � Nasazení na Streamlit Cloud

Aplikace je připravená pro nasazení na Streamlit Community Cloud. Postupujte podle [DEPLOYMENT.md](DEPLOYMENT.md) pro:

- ✅ Nastavení environment proměnných
- ✅ Konfiguraci secrets v Streamlit Cloud
- ✅ Získání Google API credentials
- ✅ Troubleshooting deployment issues

**Zkrácený postup:**

1. Push do GitHub repozitáře
2. Připojte se na [share.streamlit.io](https://share.streamlit.io)
3. Nastavte secrets v Advanced settings
4. Deploy! 🎉

## �🐛 Troubleshooting

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

### API klíč nefunguje

Zkontrolujte:

- Je environment proměnná `GOOGLE_API_KEY` nastavená?
- Má API klíč povolený Custom Search API?
- Máte ještě dostupnou kvótu (100 dotazů/den free)?

## 📜 Licence

Tento projekt je licencován pod [MIT License](LICENSE) - viz LICENSE soubor pro detaily.

## 👨‍💻 Autor

Vytvořeno s pomocí GitHub Copilot

## 🙏 Poděkování

- [Streamlit](https://streamlit.io/) za skvělý web framework
- [Google Custom Search API](https://developers.google.com/custom-search) za vyhledávací službu
- [pytest](https://pytest.org/) za testovací framework

---

**Tip**: Pro nejlepší výsledky použijte specifické vyhledávací dotazy a experimentujte s různými nastaveními lokalizace! 🚀

**Podpořte projekt**: ⭐ Dejte hvězdičku na GitHubu!
