FROM debian:bookworm
# Debian = compatibilité + apt (install simple et stable).

WORKDIR /app
# Dossier de travail dans le conteneur.

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 ca-certificates \
    && rm -rf /var/lib/apt/lists/*
# Installe Python (exécuter le serveur) + ca-certificates (HTTPS).
# Nettoyage pour réduire la taille de l’image.

ENV GAME_PORT=6000
ENV GAME_MODE=normal
# Arguments attendus (config runtime) : port + mode (surcharge via docker-compose/.env).

COPY os_server.py /app/
# Copie le code du serveur.

EXPOSE 6000
# Le service écoute en interne sur 6000 (exposition externe gérée par nginx/compose).

STOPSIGNAL SIGTERM
# Arrêt propre : docker stop envoie SIGTERM au process principal.

ENTRYPOINT ["python3"]
CMD ["/app/os_server.py"]
# Exec-form (pas /bin/sh -c) : meilleure gestion des signaux + logs.
