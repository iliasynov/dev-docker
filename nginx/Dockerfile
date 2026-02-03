FROM alpine:3.23.3

RUN apk add --no-cache nginx ca-certificates

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

STOPSIGNAL SIGTERM

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
