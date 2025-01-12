# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer les ports sur lesquels Django et FastAPI fonctionnent
EXPOSE 8000 8001

# Commande pour exécuter Django et FastAPI
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 CMDB.wsgi:application & uvicorn fast_api.main:app --host 0.0.0.0 --port 8001"]