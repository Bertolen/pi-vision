# Utiliser une image de base avec Python installé (ici l'image officielle python 3.9)
FROM python:slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de bibliothèques requises
COPY requirements.txt /app

# Mettre à jour le système et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends libgl1-mesa-glx libglib2.0-0 \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install opencv-python opencv-python-headless flask

# Copier le script Python dans le conteneur
COPY . /app

# Exposer le port (si vous prévoyez d'interagir avec une interface graphique)
EXPOSE 5000

# Commande à exécuter au démarrage du conteneur
CMD ["python", "expose_webcam.py"]

