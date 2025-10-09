# 🐳 Jak spustit na jiném PC pomocí Dockeru

## 🎯 Dva režimy spuštění:

| Režim           | Soubor                    | Použití        | Živé změny | Standalone            |
| --------------- | ------------------------- | -------------- | ---------- | --------------------- |
| **Development** | `docker-compose.yml`      | Vývoj aplikace | ✅ Ano     | ❌ Vyžaduje kód       |
| **Production**  | `docker-compose.prod.yml` | Server/sdílení | ❌ Ne      | ✅ Funguje samostatně |

---

## 🚀 Rychlý start - Development (3 kroky)

### 1️⃣ Stáhnout projekt

```bash
git clone https://github.com/Zdenal86/Google_search_export.git
cd Google_search_export
```

### 2️⃣ Vytvořit .env soubor

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Linux/Mac
cp .env.example .env
```

Otevřete `.env` v editoru a vyplňte vaše API klíče:

```env
GOOGLE_API_KEY=AIzaSyC...váš_klíč
GOOGLE_CX=0123456789...váš_cx
```

### 3️⃣ Spustit (Development)

```bash
docker-compose up -d
```

✅ Hotovo! → http://localhost:8501
🔥 **Živé změny:** Upravíte `.py` soubor → změna se projeví okamžitě

---

## 🏭 Production režim

Pro standalone container (funguje i po smazání projektu):

```bash
# Spuštění production verze
docker-compose -f docker-compose.prod.yml up -d --build

# Zastavení
docker-compose -f docker-compose.prod.yml down
```

✅ Container má kód **uvnitř** → můžete smazat projekt
❌ Změny kódu vyžadují rebuild

---

## 📚 Kompletní dokumentace

Pro detailní návod viz **[DOCKER.md](./DOCKER.md)**

---

## ⚡ Užitečné příkazy

### **Development** (docker-compose.yml)

```bash
# Spuštění
docker-compose up -d

# Zastavení
docker-compose down

# Logy
docker-compose logs -f

# Restart (po změnách v Dockerfile/requirements)
docker-compose restart

# Rebuild (po změnách v Dockerfile/requirements)
docker-compose up -d --build
```

### **Production** (docker-compose.prod.yml)

```bash
# Spuštění
docker-compose -f docker-compose.prod.yml up -d --build

# Zastavení
docker-compose -f docker-compose.prod.yml down

# Logy
docker-compose -f docker-compose.prod.yml logs -f

# Restart
docker-compose -f docker-compose.prod.yml restart
```

---

## 🔄 Přepínání mezi režimy

```bash
# Zastavit development
docker-compose down

# Spustit production
docker-compose -f docker-compose.prod.yml up -d --build
```

---

## 🔧 Troubleshooting

**Container nejede?**

```bash
docker-compose logs
```

**Port 8501 obsazený?**

```yaml
# V docker-compose.yml změňte:
ports:
  - "8502:8501"
```

**API klíče nefungují?**

```bash
# Zkontrolujte .env
cat .env  # Linux/Mac
type .env  # Windows
```

---

## 📖 Další informace

- [DOCKER.md](./DOCKER.md) - Kompletní Docker dokumentace
- [README.md](../README.md) - Dokumentace aplikace
- [DEPLOYMENT.md](./DEPLOYMENT.md) - Deploy na Streamlit Cloud
