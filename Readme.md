# PROJET — Architecture Docker Compose

Ce projet est une application multi-conteneurs composée de 4 services :
- frontend : serveur statique (HTML/CSS/JS)
- backend : API Python (FastAPI/Uvicorn)
- game : service Python (os_server)
- nginx : reverse proxy (point d’entrée unique)

![Architecture](/dev-docker.drawio.png)


Objectif : architecture isolée, reproductible et proche d’un environnement réel.


CONFIGURATION (ARGUMENTS ATTENDUS)

La configuration est externalisée via un fichier .env à la racine du projet, puis injectée dans les conteneurs avec env_file: .env et la substitution ${VAR:-default}.

Exemple de fichier .env :

## Ports
NGINX_PORT=8080

## Ressources
FRONTEND_CPUS=0.25
FRONTEND_MEM=128m
BACKEND_CPUS=0.75
BACKEND_MEM=512m
GAME_CPUS=0.50
GAME_MEM=256m
NGINX_CPUS=0.20
NGINX_MEM=128m

## Volumes (chemins dans les conteneurs)
BACKEND_DATA_PATH=/app/data
GAME_STATE_PATH=/app/state


LANCER LE PROJET

Commande :
docker compose up --build

Accès :
- Application via NGINX : http://localhost:${NGINX_PORT}

Arrêt :
docker compose down


LIMITATION DES RESSOURCES (CPU / RAM)

Chaque conteneur possède des limites (cpus, mem_limit) afin de :
- éviter qu’un service monopolise la machine,
- simuler un environnement réaliste,
- améliorer la stabilité globale.

Répartition logique :
- nginx / frontend : services légers => limites faibles
- backend / game : logique applicative => limites plus élevées


GESTION DU SIGTERM (ARRÊT PROPRE)

Lors d’un arrêt (docker stop / docker compose down), Docker envoie SIGTERM au processus principal (PID 1).
Les images utilisent des commandes en exec-form (ENTRYPOINT ["..."], CMD ["..."]) pour que le vrai processus soit PID 1 :
- meilleure propagation des signaux (SIGTERM)
- logs et codes de sortie plus fiables

Un délai de grâce (stop_grace_period) est défini dans docker-compose pour laisser le temps aux services de s’arrêter proprement avant un éventuel SIGKILL.


RÉSEAUX DOCKER

Deux réseaux sont utilisés :
- public-net : réseau “exposé” (seul nginx est accessible depuis le host via ports:)
- private-net : réseau interne pour la communication entre services (nginx ↔ backend/frontend/game)

Les services backend/frontend/game ne publient aucun port vers le host.
Ils restent accessibles uniquement via private-net.


VOLUMES DOCKER

Des volumes nommés sont utilisés pour persister les données :
- backend-data -> données backend (${BACKEND_DATA_PATH})
- game-data -> état du service game (${GAME_STATE_PATH})
- nginx-logs -> logs nginx (/var/log/nginx)

Lister les volumes :
docker volume ls

Inspecter un volume :
docker volume inspect dev-docker_backend-data
