🔵 Pourquoi Debian (bookworm)

Debian est utilisé pour les services backend (API Python, logique applicative).

Raisons principales :

Stabilité élevée
Debian est reconnu pour sa fiabilité et sa stabilité, ce qui est essentiel pour les services applicatifs long-running.

Compatibilité logicielle maximale
De nombreuses dépendances Python, bibliothèques natives et outils système sont plus facilement disponibles via apt.

Environnement proche de la production réelle
Debian est très utilisé sur les serveurs Linux professionnels, ce qui facilite le déploiement et la maintenance.

Débogage plus simple
Les outils standards (bash, curl, ip, netcat, etc.) sont facilement installables, ce qui accélère l’analyse des erreurs.

📌 Choix justifié pour les services critiques et complexes.

🟢 Pourquoi Alpine Linux

Alpine est utilisé pour les services légers (NGINX, frontend statique, petits serveurs utilitaires).

Raisons principales :

Image très légère
Alpine est basée sur musl et busybox, ce qui réduit fortement la taille des images Docker (quelques Mo).

Démarrage rapide des conteneurs
Idéal pour des services simples comme un reverse proxy ou un serveur de fichiers statiques.

Surface d’attaque réduite
Moins de paquets installés = moins de vulnérabilités potentielles.

Parfait pour les rôles “infrastructure”
NGINX ou un frontend statique n’ont pas besoin d’un OS complet.

📌 Choix optimisé pour les composants simples et performants.





Docker Cloud


frontend : react get informations from os server  and backend server

docker build -t docker-cloud-front .
docker run --rm -p 8080:8080 docker-cloud-front




backend : receive and send informations to the front

docker build -t docker-cloud-backend .
docker run --rm -p 5001:5000 docker-cloud-backend


os : only send informations to the front

docker build -t docker-cloud-game .
docker run --rm -p 6060:6000 docker-cloud-game


docker compose
docker compose up --build
go to
http://0.0.0.0:8080/



volume permet d'utiliser le meme volumese sur differents machine ,

cpu hog
memory hog
deploy resources
limit
reservation




""" TODO THIS after noone :

add the .env that contain the args
add args
add readme

learn about the entrypont and the SIGTERMs

desiner le shema de communication :

expiquer tout

"""
entrypoint ["python", "app.py"]
cmd ["--port", "5000"]


stopsignal SIGINT
