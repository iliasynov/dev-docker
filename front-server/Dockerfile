FROM ubuntu:24.04

WORKDIR /app

# Installer Python (sert juste de petit serveur web)
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

# Copier les fichiers statiques
COPY index.html /app/
COPY style.css /app/
COPY app.js /app/
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
