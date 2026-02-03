FROM debian:bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 ca-certificates \
    && rm -rf /var/lib/apt/list/*

COPY os_server.py /app/

EXPOSE 6000

CMD ["python3", "/app/os_server.py"]
