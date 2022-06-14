# flask-postgres-nginx-docker-compose
MVP repo to have default config to run flask, postgres, and nginx running and networked with docker-compose
- [Guide](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)


***
## ✨ What do you want to do? ✨
***
### ✨ Awareness ✨
[Docker](#docker) section includes sections for building, running, inspecting, and debugging docker
- Run Dev Flask Alone
    - [Dev Environment Setup](#dev-environment)
    - [Dev Docker Flask Only](#dev-docker-flask-only)

- Run Dev environment with Flask and Postgress
    - [Dev Environment Setup](#dev-environment)
    - [Dev Docker Flask And Postgress](#dev-docker-flask-and-postgress)

- Run Prod environment with Flask and Postgres
    - [Prod Environment Setup](#prod-environment)
    - [Prod Docker Flask And Postgress](#prod-docker-flask-and-postgress)


***
## ✨ Environment Setup ✨
***
### ✨ WARNING:✨  
You will need ot make sure you update any values surrounded by `<` and `>`
- e.g. change from `<db>` to `some_db_name_you_set`

### Dev Environment
- Create `.env.dev` file in root of project based on `.env.dev-sample`

### Prod Environment
- - Create `.env.prod` file in root of project based on `.env.prod-sample`


***
## ✨ Run the Services ✨ 
***
The [Docker Cleanup](#docker-cleanup) section is where I would suggest going **first** if you are getting errors before touching the code

### Dev Docker Flask Only
```shell
docker build -f ./services/web/Dockerfile -t flas-postgress-nginx:latest ./services/web

docker run -p 5001:5000 \
    -e "FLASK_APP=project/__init__.py" -e "FLASK_ENV=development" \
    flas-postgress-nginx python /usr/src/app/manage.py run -h 0.0.0.0

# cleanup
docker system prune -a -f
```

### Dev Docker Flask and Postgress
```shell
docker-compose up --build -d

#cleanup
docker-compose down -v
docker system prune -a -f
```
[Verify DB Setup](#verify-db-setup)

### Prod Docker Flask and Postgress
```shell
docker-compose -f docker-compose.prod.yml up -d --build

# database setup
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db

# cleanup
docker-compose -f docker-compose.prod.yml down -v
docker system prune -a -f
```
[Verify DB Setup](#verify-db-setup)

Optional Setup
```shell
# can create and add user to database
docker-compose exec web python manage.py seed_db
```


***
## ✨ Database ✨ 
***
### Verify Database Setup
### ✨ AWARENESS:✨  
When logging into the postgres container for dev and prod, the name will be different
- dev: `test_flask_dev` 
- prod: `test_flask_prod`
```shell
# validate database is setup and configured
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD

# verify create_db worked
test_flask_prod=# \l

# ^ Response
# Should show database created
```

### ✨ AWARENESS:✨
The Dev configuration will be the only only that sets up a `Users` table
```shell
# verify create_db worked
test_flask_dev=# \dt

# ^ Response
# Should show Users table created
```


***
## ✨ Helpful Docker Commands ✨
***
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
