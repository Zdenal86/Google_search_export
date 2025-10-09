# 🎯 Docker: Development vs Production

Tento dokument vysvětluje rozdíl mezi dvěma Docker Compose konfiguracemi.

---

## 📊 Rychlé porovnání

| Feature                         | Development            | Production                  |
| ------------------------------- | ---------------------- | --------------------------- |
| **Soubor**                      | `docker-compose.yml`   | `docker-compose.prod.yml`   |
| **Volumes**                     | ✅ Ano (`.:/app`)      | ❌ Ne                       |
| **Živé změny kódu**             | ✅ Okamžité            | ❌ Vyžaduje rebuild         |
| **Funguje po smazání projektu** | ❌ Ne                  | ✅ Ano                      |
| **Container name**              | `google-search-export` | `google-search-export-prod` |
| **Restart policy**              | `unless-stopped`       | `always`                    |
| **Ideální pro**                 | Vývoj, testování       | Server, sdílení             |
| **Přenositelnost**              | ⚠️ Nutný git clone     | ✅ Export/import image      |

---

## 🔧 Development režim

### Použití:

```bash
docker-compose up -d
```

### Konfigurace (`docker-compose.yml`):

```yaml
services:
  google-search-export:
    volumes:
      - .:/app # ← Mapuje lokální složku
    restart: unless-stopped
```

### ✅ Výhody:

- **Živé změny:** Upravíte `.py` soubor → změna se okamžitě projeví
- **Rychlý development:** Není nutný rebuild po každé změně
- **Menší build time:** Image obsahuje jen Python + knihovny

### ❌ Nevýhody:

- **Závislost na souborech:** Smažete projekt → container nefunguje
- **Není přenositelný:** Musíte mít kód lokálně
- **Bezpečnostní riziko:** Container má přístup k celé složce

### Kdy použít:

- ✅ Lokální vývoj na vašem PC
- ✅ Testování nových funkcí
- ✅ Rychlé iterace a debugování

---

## 🏭 Production režim

### Použití:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

### Konfigurace (`docker-compose.prod.yml`):

```yaml
services:
  google-search-export:
    # BEZ volumes - kód je uvnitř image
    restart: always
```

### ✅ Výhody:

- **Úplná nezávislost:** Kód je uvnitř image → funguje po smazání projektu
- **Přenositelnost:** Exportujte image, spusťte kdekoli
- **Production-ready:** Standardní pro servery
- **Bezpečnost:** Izolovaný container bez přístupu k host systému

### ❌ Nevýhody:

- **Žádné živé změny:** Každá změna kódu vyžaduje rebuild (~30s)
- **Větší image:** Obsahuje kód + Python + knihovny (~500 MB)
- **Pomalejší development:** Rebuild po každé úpravě

### Kdy použít:

- ✅ Deployment na server (VPS, cloud)
- ✅ Sdílení s kolegy (export image)
- ✅ Production prostředí
- ✅ CI/CD pipeline

---

## 🔄 Praktické workflow

### Scenario 1: Vývoj nové funkce

```bash
# Použij development režim
docker-compose up -d

# Edituj kód v IDE
# Změny se projeví okamžitě ✅

# Po dokončení
docker-compose down
```

### Scenario 2: Testování před release

```bash
# Přepni na production režim
docker-compose down
docker-compose -f docker-compose.prod.yml up -d --build

# Otestuj standalone verzi
# http://localhost:8501

# Pokud OK → ready pro deployment
docker-compose -f docker-compose.prod.yml down
```

### Scenario 3: Deployment na server

```bash
# Na serveru (Ubuntu/Debian)
git clone https://github.com/Zdenal86/Google_search_export.git
cd Google_search_export

# Vytvoř .env s klíči
nano .env

# Spusť production verzi
docker-compose -f docker-compose.prod.yml up -d --build

# Container běží samostatně
# Můžete smazat složku, container funguje ✅
```

### Scenario 4: Sdílení s kolegy

```bash
# Na vašem PC - export image
docker-compose -f docker-compose.prod.yml build
docker save -o google-search-export.tar google_search_export-google-search-export

# Přenos souboru google-search-export.tar

# Na PC kolegy - import a spuštění
docker load -i google-search-export.tar
docker run -d -p 8501:8501 \
  -e GOOGLE_API_KEY="klíč" \
  -e GOOGLE_CX="cx" \
  google_search_export-google-search-export
```

---

## 🎓 Technické detaily

### Volumes vysvětlení

**S volumes (Development):**

```
Host PC                    Docker Container
┌──────────────┐          ┌──────────────┐
│ main.py      │ ←─────→  │ /app/main.py │
│ ui.py        │ ←─────→  │ /app/ui.py   │
│ ...          │ ←─────→  │ /app/...     │
└──────────────┘          └──────────────┘
       Živé synchronizace ✅
```

**Bez volumes (Production):**

```
Host PC                    Docker Container
┌──────────────┐          ┌──────────────┐
│ main.py      │           │ main.py      │ (kopie)
│ ui.py        │    ✗      │ ui.py        │ (kopie)
│ ...          │           │ ...          │ (kopie)
└──────────────┘          └──────────────┘
       Žádná synchronizace ❌
       Container má vlastní kopii ✅
```

---

## 💡 Best Practices

### 1. **Pro development:**

- Používejte `docker-compose.yml` (s volumes)
- Commit do gitu až po otestování
- Pravidelně testujte v production režimu

### 2. **Před release:**

- Otestujte v production režimu
- Ověřte, že vše funguje bez volumes
- Zkontrolujte velikost image: `docker images`

### 3. **Pro production:**

- Používejte `docker-compose.prod.yml`
- Nikdy necommitujte `.env` s klíči
- Používejte `restart: always` pro auto-restart

### 4. **Pro CI/CD:**

- Buildujte production image
- Testujte v izolovaném containeru
- Automatizujte deployment

---

## 🔧 Přepínání mezi režimy

### Zastavit development a spustit production:

```bash
docker-compose down
docker-compose -f docker-compose.prod.yml up -d --build
```

### Zastavit production a spustit development:

```bash
docker-compose -f docker-compose.prod.yml down
docker-compose up -d
```

### Spustit oba najednou (různé porty):

```yaml
# docker-compose.yml - port 8501
# docker-compose.prod.yml - změňte na port 8502

docker-compose up -d
docker-compose -f docker-compose.prod.yml up -d --build
```

---

## 📚 Související dokumentace

- [DOCKER_QUICKSTART.md](./DOCKER_QUICKSTART.md) - Rychlý návod
- [DOCKER.md](./DOCKER.md) - Kompletní dokumentace
- [README.md](../README.md) - Dokumentace aplikace

---

## 🤔 FAQ

### Q: Musím mít oba soubory?

**A:** Ne, ale je to doporučené. Pro development stačí `docker-compose.yml`.

### Q: Jak poznám, který režim běží?

**A:**

```bash
docker ps --format "table {{.Names}}\t{{.Image}}"
# google-search-export → development
# google-search-export-prod → production
```

### Q: Můžu sdílet development container?

**A:** Ne, vyžaduje lokální soubory. Sdílejte production image.

### Q: Jak velký je rozdíl v image?

**A:** Prakticky žádný. Image obsahuje knihovny (~450 MB) + kód (~1 MB).

### Q: Který režim použít pro Streamlit Cloud?

**A:** Ani jeden. Streamlit Cloud nepotřebuje Docker, použijte přímý deployment z GitHub.

---

## 📝 Shrnutí

- **Development** = Rychlé iterace, živé změny, vyžaduje kód
- **Production** = Standalone, přenositelný, ready pro deployment
- **Oba jsou užitečné** v různých fázích vývoje
- **Přepínejte mezi nimi** podle potřeby

Doporučuji začít s **development režimem** a přejít na **production** před deploymentem! 🚀
