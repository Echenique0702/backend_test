# FastAPI User and Friendship Management API

This FastAPI application provides a CRUD interface for managing users and their friendships. The relationships between users are bidirectional, meaning that if two users are friends, this can be verified from either user’s perspective. The application is asynchronous, leverages MongoDB as the database, and is fully containerized using Docker.

## Features

### Backend

- **Framework**: FastAPI `0.111.0`
- **Language**: Python `3.12`
- **Database Driver**: Motor `3.1.1` (asynchronous version of PyMongo)

### Database

- **MongoDB Version**: `6.0.3`
- **Collections**:
  - `user_collection`: Stores user information.
  - `friendship_collection`: Stores bidirectional friendships between users.
- **Database Initialization**: On startup, the database and a non-root user with read/write access are created.

### General Characteristics

- **Dockerized Deployment**: The application uses Docker Compose for deployment, creating two containers (`api` and `mongo_database`).
- **Environment Configuration**: All environment variables are managed through a `.env` file.
- **Asynchronous Structure**:
  - `core/`: Configuration settings.
  - `database/`: MongoDB connection drivers.
  - `helpers/`: JSON conversion utilities.
  - `models/`: Data models.
  - `requirements/`: Project dependencies.
  - `routes/`: API endpoints definitions.
  - `schemas/`: Response schemas for endpoints.
  - `tests/`: Automated tests for the application.
  - `Dockerfile`: Defines the backend Docker image.
  - `main.py`: Entry point for the application.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation and Execution

1. **Configure the environment variables**:

   ```bash
   cp .env-example .env
   ```

2. **Build and execute the containers**:

   ```bash
   docker-compose up --build -d
   ```

3. **Access the API documentation**:

   **_FastAPI provides an interactive Swagger interface for exploring the API_**: [FastApi Swagguer](http://localhost:8000/docs)

### Running Tests

1. **Profile Creation**: Create a specified number of profiles in the database.

   ```bash
    docker exec -it backend_test /bin/sh -c "python tests/profile_creation.py <Number of Profiles>"
   ```

2. **Friendship Creation**: Randomly generate friendships between existing users.

   ```bash
    docker exec -it backend_test /bin/sh -c "python tests/create_relations.py <Number of Friendships>"
   ```
