FROM debian:bookworm
# Base OS Debian stable : bon compromis compatibilité / paquetages disponibles
# (apt-get disponible, utile pour python3 + venv + pip)

WORKDIR /app
# fix le repertoire de travail pour le reste des commands

# Dépendances système
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-venv python3-pip \
    && rm -rf /var/lib/apt/lists/*
# - python3 : exécuter l'application
# - python3-venv : créer un environnement virtuel isolé (bonne pratique Python)
# - python3-pip : installer les dépendances Python du projet
# - apt-get update : met à jour l'index des paquets
# - apt-get install : installe les paquets nécessaires
# - rm -rf /var/lib/apt/lists/* : nettoyage pour réduire la taille de l'image


# Create virtualenv and install deps inside it
RUN python3 -m venv /opt/venv
# évite d'installer les paquets dans le python système


ENV PATH="/opt/venv/bin:$PATH"
ENV APP_PORT=5000
ENV APP_ENV=production
# Arguments attendus :
# - PATH: force l'utilisation du python/pip du virtualenv par défaut
# - APP_PORT : port d'écoute de l'API (modifiable via docker-compose/.env)
# - APP_ENV : mode d'exécution (dev/staging/prod), utile pour logs/config


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# COPIE et install le contenue de fichier de dependances

COPY main.py /app/
# copier le code applicatif au container

EXPOSE 5000
# Documentation : indique que le conteneur écoute sur 5000


STOPSIGNAL SIGTERM
# Gestion arrêt : explicite que le conteneur doit être stoppé via SIGTERM (graceful shutdown)



ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "5000"]
# - ENTRYPOINT fixe le binaire principal (uvicorn) => le conteneur "est" un serveur uvicorn
# - CMD fournit les arguments par défaut, facilement override via docker-compose si besoin
# - Exec form (JSON array) évite /bin/sh -c et assure une bonne propagation des signaux (SIGTERM)

