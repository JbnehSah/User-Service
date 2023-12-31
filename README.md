
This prisma python project is loosly based on documentation from Python FastAPI, Prisma for python, pytest, etc and

# Prisma FastApi

[![CI](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml)


## Setup virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
```

## Install requirement

```docker-compose```

```docker```

```sh
pip install -r requirements.txt
```

## Setup environment
1. cp `.env.sample` `.env`
2. Include `DATABASE_URL`
   ```
   DATABASE_URL="postgresql://<user>:<password>@<url>:5432/postgres?schema=<scheme>"
   ```
   > Note that you should change appropriate values in `user`, `password`, `url`, `scheme` fields. Or you can even use other database. More about [connection urls](https://www.prisma.io/docs/reference/database-connectors/connection-urls)

## Generate Prisma Client and Nexus

```sh
prisma generate
```

## Start postgres as docker

```sh
docker-compose up
```


## Start server

```sh
uvicorn main:app --reload
```
## Start swagger

```sh
http://localhost/8000/docs
```

## Notes

> After installing packages

```sh
pip freeze > requirements.txt
```
