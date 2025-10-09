# Použití oficiálního Python image
FROM python:3.11-slim

# Nastavení pracovního adresáře
WORKDIR /app

# Kopírování requirements a instalace závislostí
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopírování všech souborů aplikace
COPY . .

# Expose port pro Streamlit (default 8501)
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Spuštění Streamlit aplikace
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
