# Contributing to Google Search Export

Děkujeme za tvůj zájem přispět do projektu! 🎉

## 🤝 Jak přispět

### 1. Reportování chyb (Bugs)

Pokud najdeš chybu, vytvoř **Issue** na GitHubu s těmito informacemi:

- **Popis problému** - co se stalo?
- **Kroky k reprodukci** - jak chybu vyvolat?
- **Očekávané chování** - co mělo správně fungovat?
- **Aktuální chování** - co se stalo místo toho?
- **Prostředí** - Python verze, OS, prohlížeč
- **Logy/Screenshoty** - pokud jsou dostupné

### 2. Návrhy na vylepšení (Feature Requests)

Máš nápad na novou funkcionalitu? Vytvoř Issue s:

- **Popis funkce** - co by měla dělat?
- **Use case** - proč je to užitečné?
- **Návrh implementace** (volitelné)

### 3. Pull Requesty

#### Před začátkem práce:

1. **Fork** repozitář
2. Vytvoř **novou branch** pro tvoji změnu:
   ```bash
   git checkout -b feature/moje-nova-funkce
   # nebo
   git checkout -b fix/oprava-chyby
   ```

#### Během vývoje:

1. **Formátuj kód** pomocí Black a isort:

   ```bash
   black .
   isort .
   ```

2. **Piš testy** pro novou funkcionalitu:

   - Umísti je do příslušného `test_*.py` souboru
   - Udržuj coverage nad 85% pro testované moduly

3. **Spusť testy** lokálně:

   ```bash
   pytest -v
   pytest --cov=. --cov-report=term-missing
   ```

4. **Commituj často** s popisnými commit messages:
   ```bash
   git commit -m "feat: Přidána podpora pro XYZ"
   git commit -m "fix: Opraveno chování při prázdném dotazu"
   git commit -m "docs: Aktualizace README"
   ```

#### Commit message konvence:

Používáme [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - nová funkcionalita
- `fix:` - oprava chyby
- `docs:` - změny v dokumentaci
- `style:` - formátování (bez změny logiky)
- `refactor:` - refactoring kódu
- `test:` - přidání/úprava testů
- `chore:` - build změny, dependencies

#### Před odesláním PR:

1. **Updatuj svoji branch** z `main`:

   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push** do svého forku:

   ```bash
   git push origin feature/moje-nova-funkce
   ```

3. **Vytvoř Pull Request** na GitHubu s popisem:
   - Co přidává/opravuje
   - Proč je změna potřeba
   - Jak jsi to otestoval
   - Screenshoty (pro UI změny)

## 📋 Checklist pro PR

- [ ] Kód je naformátovaný (Black, isort)
- [ ] Testy procházejí (`pytest`)
- [ ] Coverage je zachován/vylepšen
- [ ] Dokumentace je aktualizovaná
- [ ] Commit messages jsou popisné
- [ ] PR description vysvětluje změny

## 🔍 Code Review

Po vytvoření PR:

- Maintainer review kód
- Může požádat o změny
- CI musí projít (testy, linting)
- Po schválení bude PR mergnut

## 🎨 Coding Style

### Python

- Používej **PEP 8** (Black enforcement)
- Docstringy pro veřejné funkce/třídy
- Type hints kde je to vhodné
- Descriptive variable names (i když jsou české komentáře OK 🇨🇿)

### Příklad:

```python
def google_search(self, query: str, num: int = 10, language: str = "cs") -> dict:
    """
    Provede vyhledávání pomocí Google Custom Search API

    Args:
        query: Vyhledávací dotaz
        num: Počet výsledků (1-10)
        language: Jazyk výsledků (cs, en, sk, ...)

    Returns:
        dict: Google API odpověď
    """
    # Implementation...
```

## 🧪 Testování

### Struktura testů:

- `test_results_parser.py` - parsování a export
- `test_search_service.py` - Google API komunikace
- `test_ui.py` - UI komponenty

### Spuštění testů:

```bash
# Všechny testy
pytest

# S coverage
pytest --cov=. --cov-report=html

# Konkrétní soubor
pytest test_search_service.py -v

# Konkrétní test
pytest test_search_service.py::TestSearchService::test_google_search_basic -v
```

## 📚 Dokumentace

Pokud přidáváš novou funkcionalitu, aktualizuj:

- `README.md` - základní info a usage
- `DEPLOYMENT.md` - deployment info (pokud je relevantní)
- Docstringy v kódu

## ❓ Otázky?

Máš otázku? Vytvoř **Discussion** na GitHubu nebo otevři Issue s labelem `question`.

---

**Děkujeme za tvůj příspěvek! 🙏**
