FROM alpine:3.23.3
# Alpine = image légère, suffisante pour un reverse-proxy.

RUN apk add --no-cache nginx ca-certificates
# Installe nginx + certificats TLS pour connexions HTTPS. --no-cache réduit la taille de l’image.

COPY nginx.conf /etc/nginx/nginx.conf
# Copie la config (routage vers frontend/backend/game).

EXPOSE 8080
# Nginx écoute en interne sur 8080 (l’exposition au host se fait via docker-compose).

STOPSIGNAL SIGTERM
# Docker stop envoie SIGTERM → nginx peut s’arrêter proprement.

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
# Exec-form (pas /bin/sh -c) + "daemon off" garde nginx au 1er plan (sinon conteneur s’arrête).
