# flask-postgres-nginx-docker-compose
- [docker environment running flask, nginx, and postgress](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)
- configure `.env.dev` and `.env.prod` based on `.env.dev-sample` and `.env.prod-sample`


***
## ✨ flask only
***
[http://localhost:5001/](http://localhost:5001/)
```shell
docker build -f ./services/web/Dockerfile -t flas-postgress-nginx:latest ./services/web

docker run -p 5001:5000 \
    -e "FLASK_APP=project/__init__.py" \
    -e "FLASK_ENV=development" \
    -h 0.0.0.0 \
    flas-postgress-nginx \
    python \
    /usr/src/app/manage.py \
    run
    
```
```shell
# container logs
docker-compose logs -f

# wipeout
docker system prune -af
```


***
## ✨ flask and postgres
***
[http://localhost:8000/](http://localhost:8000/)
```shell
docker-compose up --build -d

# container logs
docker-compose logs -fdocker-compose -f docker-compose.prod.yml logs -f
```

```shell
# login and verify database
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD
test_flask_dev=# \l

# create user table and login to verify
docker-compose exec web python manage.py seed_db
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD
test_flask_dev=# \dt
```

```shell
# clean
docker-compose down -v
docker system prune -af
```


***
## ✨ flask postgres nginx 
***
[http://localhost:1337/static/hello.txt](http://localhost:1337/static/hello.txt)
```shell
# build and run environment 
docker-compose -f docker-compose.prod.yml up -d --build

# setup database
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

```shell
# logs
docker-compose -f docker-compose.prod.yml logs -f

# clean
docker-compose -f docker-compose.prod.yml down -v
docker system prune -af
```