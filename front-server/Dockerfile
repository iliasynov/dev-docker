FROM alpine:3.23.3

WORKDIR /app

RUN apk add --no-cache python3

ENV FRONT_PORT=80
ENV MODE=development

COPY index.html style.css app.js entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 80

STOPSIGNAL SIGTERM

ENTRYPOINT ["/app/entrypoint.sh"]
