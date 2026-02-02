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
