FROM debian:bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 ca-certificates \
    && rm -rf /var/lib/apt/list/*

ENV GAME_PORT=6000
ENV GAME_MODE=normal

COPY os_server.py /app/

EXPOSE 6000

STOPSIGNAL SIGTERM

ENTRYPOINT ["python3"]
CMD ["/app/os_server.py"]
