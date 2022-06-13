# flask-postgres-nginx-docker-compose
MVP repo to have default config to run flask, postgres, and nginx running and networked with docker-compose

## ✨ What do you want to do? ✨
### ✨ Awareness ✨
[Docker](#docker) section includes sections for building, running, inspecting, and debugging docker
- Just run the flask app on its own
    - [Dev Environment Setup](#dev-environment)
    - [Dev Docker Flask Only](#dev-docker-flask-only)

- Run Dev environment with Flask and Postgress
    - [Dev Environment Setup](#dev-environment)
    - [Dev Docker Flask And Postgress](#dev-docker-flask-and-postgress)

## ✨ Environment Setup ✨
### ✨ WARNING:✨  
You will need ot make sure you update any values surrounded by `<` and `>`
- e.g. change from `<db>` to `some_db_name_you_set`

### Dev Environment
- Create `.env.dev` file in root of project based on `.env.dev-sample`

### Prod
- TBD


## DB
### Validate Setup
TODO

## Docker
### ✨ AWARENESS:✨  
The [Docker Cleanup](#docker-cleanup) section is where I would suggest going **first** if you are getting errors before touching the code

### Dev Docker Flask Only
```shell
docker build -f ./services/web/Dockerfile -t flas-postgress-nginx:latest ./services/web

docker run -p 5001:5000 \
    -e "FLASK_APP=project/__init__.py" -e "FLASK_ENV=development" \
    flas-postgress-nginx python /usr/src/app/manage.py run -h 0.0.0.0
```
### Dev Docker Flask and Postgress
```shell
docker-compose up --build
```


### Docker Cleanup
```shell
# containers
docker rm $(docker ps -a -q)

# images
docker rmi $(docker images -a -q)

# volumes
docker-compose down -v

# system 
docker system prune
```


### Docker Helpful Commands
```shell 
# Connect to Postgresql in Docker Container
`docker-compose exec db psql --username=<POSTGRES_USER> --dbname=<POSTGRES_DB>`

# Get Volumes
`docker volume ls`

# Inspect Volume (Use output from above command to populate <volument-reference>)
`docker volume inspect <volume-reference>`
```

## Reference
- From: [Guide](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)


