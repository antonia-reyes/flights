# flights

## 0. Prerequisites

- Docker
- Docker Compose
- Environment variables in .env file (see .env.example)


## 1. Build the project

```bash
docker compose build
```


## 2. Run the project

```bash
docker compose up
```

## 3. Docs

Check the docs at http://localhost:8000/docs


# Description

This project was made with FastAPI and MongoDB, along with Docker Compose.

The project is a simple API for managing flights.

The API has the following endpoints:

- GET /flights
- GET /flights/{flight_code}
- POST /flights
- PUT /flights/{flight_code}
- DELETE /flights/{flight_code}

