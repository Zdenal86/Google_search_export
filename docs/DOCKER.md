# 🐳 Docker Deployment Guide

Tento návod vysvětluje, jak spustit Google Search Export aplikaci pomocí Dockeru na **jakémkoliv PC**.

---

## 📋 Předpoklady

Na cílovém PC musíte mít nainstalované:

1. **Docker Desktop** (Windows/Mac) nebo **Docker Engine** (Linux)

   - Windows/Mac: https://www.docker.com/products/docker-desktop
   - Linux: `sudo apt-get install docker.io docker-compose`

2. **Git** (pro stažení projektu)
   - https://git-scm.com/downloads

---

## 🎯 Dva režimy spuštění

Projekt má **dva Docker Compose soubory**:

| Režim           | Soubor                    | Účel             | Živé změny      | Standalone            |
| --------------- | ------------------------- | ---------------- | --------------- | --------------------- |
| **Development** | `docker-compose.yml`      | Vývoj, testování | ✅ Ano          | ❌ Vyžaduje kód       |
| **Production**  | `docker-compose.prod.yml` | Server, sdílení  | ❌ Ne (rebuild) | ✅ Funguje samostatně |

---

## 🚀 Rychlý start - Development

### 1. Stáhněte projekt

```bash
git clone https://github.com/Zdenal86/Google_search_export.git
cd Google_search_export
```

### 2. Nastavte API klíče

Vytvořte soubor `.env` z template:

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Linux/Mac
cp .env.example .env
```

Otevřete `.env` a vyplňte vaše Google API klíče:

```env
GOOGLE_API_KEY=AIzaSyC...váš_skutečný_klíč
GOOGLE_CX=0123456789abc...váš_cx_id
```

> ⚠️ **DŮLEŽITÉ**: Soubor `.env` není v gitu! Každý uživatel si ho musí vytvořit lokálně.

### 3. Spusťte aplikaci (Development)

```bash
docker-compose up -d
```

✅ **Hotovo!** Aplikace běží na http://localhost:8501

🔥 **Živé změny:** Upravíte `.py` soubor → změna se projeví okamžitě (díky volumes)

---

## 🏭 Production režim

Pro standalone container, který funguje i po smazání projektu:

```bash
# Build a spuštění production verze
docker-compose -f docker-compose.prod.yml up -d --build
```

✅ **Výhody:**

- Kód je **uvnitř** image → můžete smazat projekt
- Container je **přenositelný** (export/import image)
- **Production-ready** pro servery

❌ **Nevýhody:**

- Změny kódu vyžadují **rebuild** (~30s)
- Větší image (~500 MB s kódem)

### Export/Import image (bez git clone)

```bash
# Export image do souboru
docker save -o google-search-export.tar google_search_export-google-search-export

# Přenos na jiný PC a import
docker load -i google-search-export.tar

# Spuštění (s vlastním .env)
docker run -d -p 8501:8501 \
  -e GOOGLE_API_KEY="váš_klíč" \
  -e GOOGLE_CX="váš_cx" \
  --name google-search-export \
  google_search_export-google-search-export
```

---

## 📦 Podrobné příkazy

### **Development režim** (docker-compose.yml)

```bash
# Build a spuštění
docker-compose up -d

# Zastavení
docker-compose down

# Restart (bez rebuildu)
docker-compose restart

# Rebuild (po změnách Dockerfile/requirements.txt)
docker-compose up -d --build

# Logy
docker-compose logs -f
```

### **Production režim** (docker-compose.prod.yml)

```bash
# Build a spuštění
docker-compose -f docker-compose.prod.yml up -d --build

# Zastavení
docker-compose -f docker-compose.prod.yml down

# Restart
docker-compose -f docker-compose.prod.yml restart

# Logy
docker-compose -f docker-compose.prod.yml logs -f
```

### **Přepínání mezi režimy**

```bash
# Zastavit development
docker-compose down

# Spustit production
docker-compose -f docker-compose.prod.yml up -d --build

# Nebo naopak
docker-compose -f docker-compose.prod.yml down
docker-compose up -d
```

### Kontrola stavu

```bash
# Seznam běžících containerů
docker ps

# Detaily o containeru
docker inspect google-search-export

# Healthcheck status
docker inspect --format='{{.State.Health.Status}}' google-search-export
```

---

## 🔧 Konfigurace

### Environment proměnné

V `docker-compose.yml` se načítají z lokálního `.env`:

```yaml
environment:
  - GOOGLE_API_KEY=${GOOGLE_API_KEY}
  - GOOGLE_CX=${GOOGLE_CX}
```

### Porty

Výchozí port je `8501`. Změna:

```yaml
ports:
  - "3000:8501" # Aplikace dostupná na http://localhost:3000
```

### Volumes - Development vs Production

#### **Development** (`docker-compose.yml`)

```yaml
volumes:
  - .:/app # Mapuje lokální adresář do containeru
```

✅ **Výhody:** Živé změny kódu, rychlý development
❌ **Nevýhody:** Vyžaduje lokální soubory, není přenositelný

#### **Production** (`docker-compose.prod.yml`)

```yaml
# BEZ volumes - kód je uvnitř image
```

✅ **Výhody:** Standalone, přenositelný, funguje po smazání projektu
❌ **Nevýhody:** Změny vyžadují rebuild

---

## 🔄 Výhody a nevýhody režimů

| Feature                         | Development        | Production               |
| ------------------------------- | ------------------ | ------------------------ |
| **Živé změny kódu**             | ✅ Ano (volumes)   | ❌ Ne (rebuild nutný)    |
| **Funguje po smazání projektu** | ❌ Ne              | ✅ Ano                   |
| **Rychlost vývoje**             | ⭐⭐⭐⭐⭐         | ⭐⭐                     |
| **Přenositelnost**              | ❌ Nutný git clone | ✅ Export/import image   |
| **Velikost image**              | ~500 MB (knihovny) | ~500 MB (knihovny + kód) |
| **Ideální pro**                 | Lokální vývoj      | Server, sdílení          |

---

## 🏗️ Architektura

```
┌─────────────────────────────────────────┐
│         Docker Container                │
│  ┌───────────────────────────────────┐  │
│  │   Streamlit App (port 8501)       │  │
│  │   - main.py                       │  │
│  │   - search_service.py             │  │
│  │   - ui.py                         │  │
│  └───────────────────────────────────┘  │
│              ▲                          │
│              │ Environment Variables    │
└──────────────┼──────────────────────────┘
               │
          ┌────┴─────┐
          │  .env    │ ← Lokální soubor (není v gitu)
          └──────────┘
```

---

## 🐛 Troubleshooting

### Container se nespustí

```bash
# Zkontrolujte logy
docker-compose logs

# Zkontrolujte .env soubor
cat .env  # Linux/Mac
type .env  # Windows

# Rebuild bez cache
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Port 8501 už používá jiná aplikace

Buď:

1. Zastavte aplikaci na portu 8501
2. Nebo změňte port v `docker-compose.yml`:

```yaml
ports:
  - "8502:8501" # Použije port 8502
```

### API klíče nefungují

```bash
# Zkontrolujte, že se načítají
docker exec google-search-export printenv | grep GOOGLE

# Měli byste vidět:
# GOOGLE_API_KEY=AIza...
# GOOGLE_CX=012345...
```

Pokud jsou prázdné → zkontrolujte `.env` soubor.

### Healthcheck failing

```bash
# Manuálně nainstalovat curl do containeru
docker exec google-search-export apt-get update
docker exec google-search-export apt-get install -y curl

# Nebo upravte Dockerfile:
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
```

---

## 🌐 Deploy na server

### 1. Produkční Docker Compose

Vytvořte `docker-compose.prod.yml`:

```yaml
version: "3.8"

services:
  google-search-export:
    build: .
    container_name: google-search-export
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - GOOGLE_CX=${GOOGLE_CX}
    restart: always # Auto-restart při pádu
    # volumes:  # BEZ volume v produkci
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2. Spuštění na serveru

```bash
# Na serveru (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y docker.io docker-compose git

# Clone projektu
git clone https://github.com/Zdenal86/Google_search_export.git
cd Google_search_export

# Vytvoření .env s klíči
nano .env

# Build a spuštění
docker-compose -f docker-compose.prod.yml up -d

# Kontrola
docker ps
curl http://localhost:8501
```

### 3. Nginx reverse proxy (volitelné)

Pro HTTPS a custom doménu:

```nginx
server {
    listen 80;
    server_name search.example.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

---

## 📊 Monitoring

### Využití zdrojů

```bash
# CPU, RAM, Network
docker stats google-search-export

# Disk space
docker system df
```

### Auto-restart

Container se automaticky restartuje při pádu díky:

```yaml
restart: unless-stopped
```

---

## 🔒 Bezpečnost

### ✅ Dobré praktiky

1. **`.env` není v gitu** → každý uživatel má vlastní klíče
2. **`.dockerignore`** → secrets se nedostanou do image
3. **Healthcheck** → sledování dostupnosti aplikace
4. **Non-root user** (volitelné):

```dockerfile
# Přidejte do Dockerfile před CMD
RUN useradd -m -u 1000 appuser
USER appuser
```

### ❌ Nedělat

- ❌ Necommitujte `.env` do gitu
- ❌ Neukládejte klíče přímo do `docker-compose.yml`
- ❌ Nesdílejte Docker image s API klíči

---

## 🆚 Docker vs. Klasické spuštění

| Feature   | Docker              | Klasické (venv)                   |
| --------- | ------------------- | --------------------------------- |
| Instalace | `docker-compose up` | `pip install -r requirements.txt` |
| Izolace   | ✅ Úplná            | ⚠️ Závisí na venv                 |
| Portable  | ✅ Funguje všude    | ⚠️ Problém s Python verzemi       |
| Velikost  | ~500 MB (image)     | ~50 MB (venv)                     |
| Start     | ~3 sekundy          | ~1 sekunda                        |
| Update    | Rebuild image       | `pip install -U`                  |

---

## 💡 Pro-tipy

1. **Multi-stage build** (menší image):

   ```dockerfile
   FROM python:3.11-slim as builder
   # ... build dependencies
   FROM python:3.11-slim
   COPY --from=builder /app /app
   ```

2. **Docker secrets** (místo .env):

   ```bash
   echo "AIzaSy..." | docker secret create google_api_key -
   ```

3. **Compose watch** (auto-reload):
   ```bash
   docker-compose watch
   ```

---

## 📚 Odkazy

- 📖 [Docker Documentation](https://docs.docker.com/)
- 🐳 [Docker Hub](https://hub.docker.com/)
- 🎯 [Streamlit Docker Guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)
- 🔐 [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/)

---

## 📝 Changelog

- **v1.0** (2025-01-09): Initial Docker setup
  - Dockerfile s Python 3.11
  - docker-compose.yml s environment variables
  - .dockerignore pro bezpečnost
  - Kompletní dokumentace

---

## 🤝 Podpora

Pokud máte problém s Docker setupem:

1. Zkontrolujte [Troubleshooting](#-troubleshooting)
2. Otevřete issue na GitHub
3. Připojte logy: `docker-compose logs > logs.txt`
