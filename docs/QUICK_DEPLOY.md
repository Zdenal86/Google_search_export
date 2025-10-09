# ⚡ Rychlý návod: Nasazení na Streamlit Cloud

## 🎯 Krok za krokem (5 minut)

### 1️⃣ Přihlas se
- Jdi na: **https://share.streamlit.io/**
- Přihlaš se přes **GitHub** (Zdenal86)

---

### 2️⃣ Vytvoř novou aplikaci
Klikni **"New app"** a vyplň:
```
Repository: Zdenal86/Google_search_export
Branch: main
Main file path: main.py
```

---

### 3️⃣ Nastav Secrets (DŮLEŽITÉ! 🔐)
V sekci **"Advanced settings"** → **"Secrets"** vlož:

```toml
GOOGLE_API_KEY = "tvůj-api-key"
GOOGLE_CX = "tvůj-cx-id"
```

**Kde vzít credentials?**
- API Key: [Google Cloud Console](https://console.cloud.google.com/) → API & Services → Credentials
- CX: [Programmable Search Engine](https://programmablesearchengine.google.com/) → Edit search engine → Engine ID

---

### 4️⃣ Deploy!
Klikni **"Deploy"** a počkej ~2 minuty. Hotovo! 🎉

---

## 🔄 Aktualizace aplikace

Každý `git push` na `main` branch = automatický redeploy!

```bash
git add .
git commit -m "Update"
git push
```

---

## 🐛 Problémy?

**App spadne:**
- Zkontroluj Secrets (Settings → Secrets)
- Zkontroluj formát: `KLÍČ = "hodnota"` (s uvozovkami!)

**Logs:**
- Dashboard → tvoje app → "Manage app" → "Logs"

---

## 📱 Tvoje app URL

Po nasazení:
```
https://tvoje-app-name.streamlit.app
```

**Hotovo!** ✨
