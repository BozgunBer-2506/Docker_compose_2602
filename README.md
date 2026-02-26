# FastAPI and PostgreSQL with Docker Compose

This is a multi-container application using **FastAPI** as the backend and **PostgreSQL** as the database.

## Prerequisites
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd compose-app

```

2. **Create a `.env` file:**
Create a file named `.env` in the root directory and add your credentials:
```text
DB_USER=admin
DB_PASSWORD=your_secure_password
DB_NAME=app_db

```


3. **Start the application:**
```bash
docker compose up -d --build

```


4. **Access the API:**
Open your browser and go to: `http://localhost:8000`

## Features

* **Persistence:** Database stays safe in a Docker Volume.
* **Healthcheck:** API waits for the Database to be ready.
* **Security:** Credentials managed via environment variables.

## Cleanup

To stop and remove containers:

```bash
docker compose down

```

