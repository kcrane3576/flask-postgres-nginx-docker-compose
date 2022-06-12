# flask-postgres-nginx-docker-compose
MVP repo to have default config to run flask, postgres, and nginx running and networked with docker-compose

## Prerequisites
- Create `.env.dev` file in root of project based on `.env.dev-sample`

## Local
- `docker-compose up`
- Go to url: [http://localhost:8000/](http://localhost:8000/)


## Docker cleanup
### Cleanup Containers
`docker rm $(docker ps -a -q)`

### Cleanup Images
`docker rmi $(docker images -a -q)`

### Cleanup System
`docker system prune`

### Reference
- From: [blog](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)