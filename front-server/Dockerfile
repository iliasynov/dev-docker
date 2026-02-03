FROM alpine:3.23.3

WORKDIR /app

RUN apk add --no-cache python3

COPY index.html style.css app.js entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 80
ENTRYPOINT ["/app/entrypoint.sh"]
