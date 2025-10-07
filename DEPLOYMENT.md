# 🚀 Deployment Guide - Streamlit Community Cloud# 🚀 Nasazení na Streamlit Community Cloud

Tento návod tě provede nasazením aplikace na **Streamlit Community Cloud** (zdarma).Tento návod vám pomůže nasadit vyhledávací aplikaci na Streamlit Community Cloud.

---## 📋 Prerekvizity

## 📋 Před nasazením1. **GitHub repozitář** - Aplikace musí být v GitHub repozitáři

2. **Streamlit účet** - Zaregistrujte se na [share.streamlit.io](https://share.streamlit.io)

### 1. Ujisti se, že máš GitHub repozitář3. **Google API credentials** - API klíč a Custom Search Engine ID

✅ Tvůj kód je už na GitHubu: `https://github.com/Zdenal86/Google_search_export`

## 🔑 Konfigurace Secrets

### 2. Zkontroluj potřebné soubory

✅ `main.py` - vstupní bod aplikace### 1. Příprava credentials

✅ `requirements.txt` - závislosti (minimální verze)

✅ `.gitignore` - obsahuje `.streamlit/secrets.toml`Aplikace vyžaduje dva secrets:

---- `GOOGLE_API_KEY` - Váš Google Custom Search API klíč

- `GOOGLE_CX` - Custom Search Engine ID (cx)

## 🔐 Krok 1: Připrav Google API credentials

### 2. Nastavení v Streamlit Cloud

### Pokud ještě nemáš Google API Key a CX:

1. Přihlaste se na [share.streamlit.io](https://share.streamlit.io)

1. **Google API Key:**2. Klikněte na **"New app"**

   - Jdi na [Google Cloud Console](https://console.cloud.google.com/)3. Vyberte váš GitHub repozitář a branch

   - Vytvoř nový projekt (nebo vyber existující)4. Nastavte **Main file path**: `main.py`

   - Zapni **Custom Search API**5. Klikněte na **"Advanced settings"**

   - Vytvoř **API Key** v sekci "Credentials"6. V sekci **"Secrets"** přidejte následující:

1. **Google CX (Search Engine ID):**```toml

   - Jdi na [Programmable Search Engine](https://programmablesearchengine.google.com/)GOOGLE_API_KEY = "váš-google-api-klíč"

   - Klikni "Add" → vytvoř nový search engineGOOGLE_CX = "váš-cx-id"

   - V nastaveních najdi **Search engine ID (CX)**```

---7. Klikněte na **"Deploy!"**

## ☁️ Krok 2: Nasazení na Streamlit Cloud### 3. Alternativa - Secrets management přes Dashboard

### 1. Přihlas se na Streamlit CloudPo nasazení můžete secrets upravit v nastavení aplikace:

Jdi na: **https://share.streamlit.io/**1. Otevřete váš app na Streamlit Cloud

2. Klikněte na **☰** menu (vpravo nahoře)

Přihlas se pomocí svého **GitHub účtu** (Zdenal86).3. Vyberte **"Settings"**

4. Přejděte na **"Secrets"**

---5. Upravte secrets ve formátu TOML

### 2. Vytvoř novou aplikaci## 🔐 Bezpečnost

1. Klikni na **"New app"** (nebo "Create app")⚠️ **DŮLEŽITÉ:**

2. Vyplň deployment formulář:- Nikdy necommitujte API klíče do Git repozitáře

   ```- Soubor `.streamlit/secrets.toml`je v`.gitignore`

   Repository: Zdenal86/Google_search_export- Pro produkci vždy používejte environment proměnné nebo Streamlit secrets

   Branch: main

   Main file path: main.py## 🏠 Lokální vývoj

   ```

   ```

Pro lokální testování můžete použít:

3. **App URL** (volitelné):

   - Můžeš si vybrat vlastní subdoménu, např:### Option 1: `.streamlit/secrets.toml` (doporučeno)

   - `https://your-app-name.streamlit.app`

````toml

---GOOGLE_API_KEY = "váš-api-klíč"

GOOGLE_CX = "váš-cx"

### 3. Nastav Secrets (důležité! 🔐)```



Před spuštěním aplikace **musíš nastavit secrets**:### Option 2: Environment proměnné



1. V deployment formuláři najdi sekci **"Advanced settings"** → **"Secrets"**```powershell

# PowerShell

2. Do pole "Secrets" vlož:$env:GOOGLE_API_KEY = "váš-api-klíč"

   ```toml$env:GOOGLE_CX = "váš-cx"

   GOOGLE_API_KEY = "tvůj-google-api-key"streamlit run main.py

   GOOGLE_CX = "tvůj-cx-id"```

````

````bash

   **Příklad:**# Linux/Mac

   ```tomlexport GOOGLE_API_KEY="váš-api-klíč"

   GOOGLE_API_KEY = "AIzaSyAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPp"export GOOGLE_CX="váš-cx"

   GOOGLE_CX = "a1b2c3d4e5f6g7h8i"streamlit run main.py

````

3. Klikni **"Save"**### Option 3: Fallback hodnoty v kódu

---Pokud environment proměnné nejsou nastaveny, aplikace použije fallback hodnoty v `search_service.py`

### 4. Deploy!## 📚 Získání Google API credentials

Klikni na **"Deploy!"** (nebo "Deploy app")### Google Custom Search API klíč

Streamlit Cloud teď:1. Přejděte na [Google Cloud Console](https://console.cloud.google.com/)

- ✅ Naklonuje tvůj GitHub repozitář2. Vytvořte nový projekt nebo vyberte existující

- ✅ Nainstaluje závislosti z `requirements.txt`3. Povolte **Custom Search API**

- ✅ Spustí `main.py`4. Vytvořte API klíč v sekci **"Credentials"**

- ✅ Aplikace bude dostupná na tvé URL

### Custom Search Engine ID (CX)

---

1. Přejděte na [Programmable Search Engine](https://programmablesearchengine.google.com/)

## 🎉 Hotovo!2. Vytvořte nový vyhledávač nebo upravte existující

3. Zkopírujte **Search engine ID** (cx)

Tvoje aplikace je živá! Měla by běžet na:

````## 🔄 Update aplikace

https://your-app-name.streamlit.app

```Po změnách v kódu:



---1. Pushněte změny do GitHub repozitáře

2. Streamlit Cloud automaticky detekuje změny a redeployuje aplikaci

## 🔧 Aktualizace aplikace

## 📊 Monitoring

### Automatické aktualizace

Kdykoli pushneš změny do `main` branch na GitHubu, **Streamlit Cloud automaticky redeployuje** aplikaci!- **Logs**: Dostupné v Streamlit Cloud dashboardu

- **Usage**: Sledujte využití API na [Google Cloud Console](https://console.cloud.google.com/)

```bash

git add .## 🆘 Troubleshooting

git commit -m "feat: Nová funkce"

git push### Aplikace nefunguje po nasazení

````

- Zkontrolujte, že secrets jsou správně nastaveny

Po pár sekundách bude nová verze živá! 🚀- Ověřte logy v Streamlit Cloud dashboardu

- Zkontrolujte, že API klíč má povolený Custom Search API

### Ruční redeployment

V dashboard Streamlit Cloud můžeš kliknout na **"Reboot app"** nebo **"Manage app"** → **"Reboot"**.### API quota exceeded

---- Google Custom Search má limit 100 dotazů/den v free tier

- Zvažte upgrade plánu nebo optimalizaci dotazů

## 🐛 Řešení problémů

### Secrets se nenačítají

### Problém: Aplikace spadne s chybou "GOOGLE_API_KEY not found"

**Řešení:** Zkontroluj, že jsi správně nastavil secrets v Streamlit Cloud:- Zkontrolujte formát TOML (název = "hodnota")

1. Jdi do dashboard → tvoje app → **"Settings"** → **"Secrets"**- Ujistěte se, že názvy odpovídají těm v kódu

2. Zkontroluj formát (TOML):- Redeployujte aplikaci po změně secrets

   ````toml

   GOOGLE_API_KEY = "value"## 📝 Další zdroje

   GOOGLE_CX = "value"

   ```- [Streamlit Community Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
   ````

- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)

### Problém: Dependency install error- [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction)

**Řešení:** Zkontroluj `requirements.txt`:

- Měl by obsahovat jen **runtime dependencies**
- Verze by měly být kompatibilní s Python 3.10+

### Problém: Aplikace je pomalá

**Řešení:**

- Streamlit Community Cloud má **omezené prostředky** (zdarma)
- Omezte počet vyhledávání nebo cachujte výsledky pomocí `@st.cache_data`

---

## 📊 Monitoring

V Streamlit Cloud dashboard můžeš sledovat:

- 📈 **Logs** - živé logy aplikace
- 💾 **Resource usage** - CPU/RAM využití
- 👥 **Analytics** - počet návštěvníků (pokud je zapnuto)

---

## 🔒 Bezpečnost

### ✅ Co je bezpečné:

- ✅ `.streamlit/secrets.toml` je v `.gitignore` (nikdy commitnutý)
- ✅ GitHub Secrets jsou v repo settings (pro CI)
- ✅ Streamlit Cloud secrets jsou oddělené

### ⚠️ Nikdy nedělej:

- ❌ Necommituj `secrets.toml` do gitu
- ❌ Nevkládej API keys přímo do kódu
- ❌ Nesdílej screenshot s viditelnými secrets

---

## 🎯 Pro-tipy

1. **Custom doména:**

   - V Streamlit Cloud (platená verze) můžeš mít vlastní doménu

2. **GitHub Badge:**

   - Přidej deployment badge do README:
     ```markdown
     [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
     ```

3. **Auto-updates:**
   - Každý push do `main` = automatický redeploy
   - Pro staging použij branch `develop` a nasaď jako samostatnou app

---

## 📚 Další zdroje

- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [GitHub Integration](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

---

**Hodně štěstí s nasazením! 🚀**

Pokud máš problémy, otevři issue na GitHubu nebo se podívej do logů v Streamlit Cloud dashboard.
