FROM alpine:3.23.3
# Base Alpine : image légère (petite taille), suffisante pour servir des fichiers statiques.
# apk = gestionnaire de paquets d'Alpine (équivalent apt sur Debian).

WORKDIR /app
# Manipulation OS : définit le répertoire de travail.
# Toutes les copies/commandes suivantes se font dans /app.

RUN apk add --no-cache python3
# Dépendances installées :
# - python3 : utilisé ici comme petit serveur HTTP (python -m http.server).
# Manipulation OS :
# - apk add : installe les paquets
# - --no-cache : évite de garder le cache des paquets => image plus légère.

ENV FRONT_PORT=80
ENV MODE=development
# Arguments attendus (runtime config) :
# - FRONT_PORT : port sur lequel le serveur statique écoute dans le conteneur
# - MODE : permet de distinguer dev/prod (logs, comportements éventuels, etc.)
# Ces valeurs peuvent être surchargées par docker-compose/.env.

COPY index.html style.css app.js entrypoint.sh /app/
# Manipulation OS : copie des fichiers statiques + script de démarrage dans l'image.

RUN chmod +x /app/entrypoint.sh
# Manipulation OS : rend le script exécutable (permission Unix).

EXPOSE 80
# Documentation : indique le port attendu dans le conteneur.
# (N'expose pas automatiquement au host ; c'est docker-compose/nginx qui gère l'accès externe.)

STOPSIGNAL SIGTERM
# Gestion arrêt : rend explicite que l'arrêt doit se faire via SIGTERM (arrêt propre).
# Docker utilise SIGTERM par défaut ; ici on l'affiche clairement pour la compréhension/notation.

ENTRYPOINT ["/app/entrypoint.sh"]
# Choix ENTRYPOINT :
# - On utilise un script pour valider/configurer le runtime (FRONT_PORT, MODE)
# - Et surtout pour lancer le serveur avec "exec" afin que le vrai processus devienne PID 1 :
#   => SIGTERM est bien reçu, et les crashes sont plus faciles à diagnostiquer.
