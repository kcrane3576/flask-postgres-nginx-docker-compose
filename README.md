# flask-postgres-nginx-docker-compose
MVP repo to have default config to run flask, postgres, and nginx running and networked with docker-compose
- [Guide](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)


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

### Prod Environment
- - Create `.env.prod` file in root of project based on `.env.prod-sample`


## DB
### Validate Setup
- Log into the postgres container
- Verify the database was created
```shell
# for this project POSTGRES_DB will be either test_flask_dev or test_flask_prod
`docker-compose exec db psql --username=<POSTGRES_USER> --dbname=<POSTGRES_DB>`
# verify database setup
\l
```


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

# validate database is setup and configured
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD

# verify create_db worked
test_flask_dev=# \l

# ^ Response
# Should show list of databases and there should be a test_flask_dev database
```

Optional Setup
```shell
# can create and add user to database
docker-compose exec web python manage.py seed_db
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
# get docker logs
docker compose logs -f 

# Connect to Postgresql in Docker Container
`docker-compose exec db psql --username=<POSTGRES_USER> --dbname=<POSTGRES_DB>`

# Get Volumes
`docker volume ls`

# Inspect Volume (Use output from above command to populate <volument-reference>)
`docker volume inspect <volume-reference>`
```


