# Docker Flask & PostgresSql

## Installation

```bash
docker-compose up -d --build
```

## Features

* Full **Docker** integration (Docker based)
* **Docker Compose** integration and optimization for local development
* **Production ready** Python web server using Nginx and uWSGI
* Python **Flask** backend with:
  * **Sentry**: Tracks errors in all major languages & frameworks
  * **ApiDoc**: Swagger live documentation generation
  * **Webargs**: parse, validate and document inputs to the endpoint / route
  * **Secure password** hashing by default
  * **JWT token** authentication
  * **SQLAlchemy** models (independent of Flask extensions, so they can be used with Celery workers directly)
  * Basic starting models for users and groups (modify and remove as you need)
  * **Alembic** migrations
  * **CORS** (Cross Origin Resource Sharing)
* REST backend tests based on **Pytest**, integrated with Docker, so you can test the full API interaction, independent on the database. As it runs in Docker, it can build a new data store from scratch each time (so you can use ElasticSearch, MongoDB, CouchDB, or whatever you want, and just test that the API works)
* Easy Python integration with **Jupyter Kernels** for remote or in-Docker development with extensions like Atom Hydrogen or Visual Studio Code Jupyter