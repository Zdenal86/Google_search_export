# 🔍 Vyhledávací aplikace

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://search-export.streamlit.app/)
[![Tests](https://github.com/Zdenal86/Google_search_export/actions/workflows/tests.yml/badge.svg)](https://github.com/Zdenal86/Google_search_export/actions/workflows/tests.yml)
[![Quick CI](https://github.com/Zdenal86/Google_search_export/actions/workflows/quick-ci.yml/badge.svg)](https://github.com/Zdenal86/Google_search_export/actions/workflows/quick-ci.yml)
[![Code Quality](https://github.com/Zdenal86/Google_search_export/actions/workflows/code-quality.yml/badge.svg)](https://github.com/Zdenal86/Google_search_export/actions/workflows/code-quality.yml)
[![codecov](https://codecov.io/gh/Zdenal86/Google_search_export/branch/main/graph/badge.svg)](https://codecov.io/gh/Zdenal86/Google_search_export)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Jednoduchá webová aplikace pro vyhledávání pomocí Google Custom Search API s podporou lokalizace.

## 🚀 Živá aplikace

**Vyzkoušej aplikaci online:** **https://search-export.streamlit.app/**

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

## ⚡ Quick Start - Streamlit Cloud

Nejrychlejší způsob, jak dostat aplikaci do provozu:

### 1️⃣ Jdi na [share.streamlit.io](https://share.streamlit.io/)

Přihlaš se přes GitHub

### 2️⃣ Vytvoř novou app

```
Repository: Zdenal86/Google_search_export
Branch: main
Main file: main.py
```

### 3️⃣ Nastav Secrets (⚠️ DŮLEŽITÉ!)

V "Advanced settings" → "Secrets":

```toml
GOOGLE_API_KEY = "tvůj-api-key"
GOOGLE_CX = "tvůj-cx-id"
```

**Kde získat credentials?**

- **API Key:** [Google Cloud Console](https://console.cloud.google.com/) → API & Services → Credentials → Create API Key
- **CX ID:** [Programmable Search Engine](https://programmablesearchengine.google.com/) → Edit → Engine ID

### 4️⃣ Deploy! 🚀

Hotovo za ~2 minuty! Aplikace bude na `https://tvoje-app.streamlit.app`

> 📖 Detailní návod: [QUICK_DEPLOY.md](QUICK_DEPLOY.md)

---

## 🚀 Lokální instalace

### 1. Klonování repozitáře

```bash
git clone https://github.com/Zdenal86/Google_search_export.git
cd Google_search_export
```

### 2. Vytvoření virtual environmentu

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalace závislostí

```powershell
# Minimální instalace (pro běh aplikace)
pip install -r requirements-minimal.txt

# Plná instalace (včetně dev nástrojů)
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Konfigurace API credentials

#### Varianta A: Streamlit Secrets (doporučeno)

Vytvoř `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "tvůj-google-api-klíč"
GOOGLE_CX = "tvůj-cx-id"
```

#### Varianta B: Environment proměnné

```powershell
$env:GOOGLE_API_KEY = "tvůj-api-klíč"
$env:GOOGLE_CX = "tvůj-cx"
```

> 💡 **Tip:** Zkopíruj `.streamlit/secrets.toml.example` a uprav hodnoty
>
> 📚 Podrobný návod na získání credentials: [DEPLOYMENT.md](DEPLOYMENT.md)

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

## 🐛 Troubleshooting & Error Handling

### Chybějící API credentials

**Problém:**

```
AttributeError: 'NoneType' object has no attribute 'cse'
```

**Řešení:** API klíče nejsou nastavené. Zkontroluj:

```powershell
# Streamlit Cloud: Settings → Secrets
# Lokálně: .streamlit/secrets.toml nebo environment proměnné
```

### Google API Error Responses

**429 Too Many Requests**

```json
{
  "error": {
    "code": 429,
    "message": "Quota exceeded for quota metric 'Queries' and limit 'Queries per day'"
  }
}
```

**Řešení:** Překročen denní limit (100 queries/den zdarma). Počkej 24h nebo upgraduj na placenou verzi.

**403 Forbidden**

```json
{
  "error": {
    "code": 403,
    "message": "The request is missing a valid API key."
  }
}
```

**Řešení:** Neplatný nebo chybějící API klíč. Zkontroluj `GOOGLE_API_KEY` v secrets.

**400 Bad Request - Invalid CX**

```json
{
  "error": {
    "code": 400,
    "message": "Invalid Value"
  }
}
```

**Řešení:** Neplatný CX (Search Engine ID). Ověř `GOOGLE_CX` v [Programmable Search Engine](https://programmablesearchengine.google.com/).

### Deployment problémy

**Streamlit Cloud: App crashes on startup**

1. **Zkontroluj logs:** Dashboard → Manage app → Logs
2. **Ověř secrets formát:**
   ```toml
   GOOGLE_API_KEY = "hodnota"  # S uvozovkami!
   GOOGLE_CX = "hodnota"
   ```
3. **Zkontroluj requirements.txt:** Všechny dependencies přítomné?

**Streamlit Cloud: Slow performance**

Free tier má omezené resources:

- Cache API responses: `@st.cache_data(ttl=3600)`
- Limit počet výsledků: `num=5` místo `num=10`

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

### Coverage pod 85%

Pokud přidáváš kód do `search_service.py` nebo `results_parser.py`, přidej testy!
UI moduly (`main.py`, `ui.py`) jsou vyloučeny z coverage (`.coveragerc`).

### API klíč nefunguje

Zkontrolujte:

- Je environment proměnná `GOOGLE_API_KEY` nastavená?
- Má API klíč povolený Custom Search API?
- Máte ještě dostupnou kvótu (100 dotazů/den free)?

## 🤝 Contributing

Příspěvky jsou vítány! Před tím, než začneš:

1. 📖 Přečti si [CONTRIBUTING.md](CONTRIBUTING.md) - guide jak přispívat
2. 📜 Dodržuj [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - pravidla chování
3. 🐛 Reportuj bugy nebo navrhuj features přes [GitHub Issues](https://github.com/Zdenal86/Google_search_export/issues)
4. 🔀 Vytvoř Pull Request s popisem změn

**Quick checklist pro PR:**

- [ ] Kód naformátovaný (`black .`, `isort .`)
- [ ] Testy procházejí (`pytest`)
- [ ] Coverage zachován/vylepšen
- [ ] Dokumentace aktualizovaná

## 📜 Licence

Tento projekt je licencován pod [MIT License](LICENSE) - viz LICENSE soubor pro detaily.

## 👨‍💻 Autor

Vytvořeno s pomocí GitHub Copilot

## 🙏 Poděkování

- [Streamlit](https://streamlit.io/) za skvělý web framework
- [Google Custom Search API](https://developers.google.com/custom-search) za vyhledávací službu
- [pytest](https://pytest.org/) za testovací framework
- Všem [contributors](https://github.com/Zdenal86/Google_search_export/graphs/contributors) 🎉

---

**Tip**: Pro nejlepší výsledky použijte specifické vyhledávací dotazy a experimentujte s různými nastaveními lokalizace! 🚀

**Podpořte projekt**: ⭐ Dejte hvězdičku na GitHubu!
