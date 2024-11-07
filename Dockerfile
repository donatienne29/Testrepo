# Utiliser une image Python de base
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Exposer le port sur lequel Flask fonctionne
EXPOSE 5000

# Démarrer l'application
CMD ["python3", "app.py"]
