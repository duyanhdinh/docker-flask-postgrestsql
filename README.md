# Docker Flask & PostgresSql
docker for flask postgrestsql base on [tiangolo/full-stack](https://github.com/tiangolo/full-stack)

## Installation

```bash
docker-compose up -d --build
```

## Features

* Full **Docker** integration (Docker based) with:
  * **Flask**: as Python web server
  * **PostgresSQL**: as database
* **Docker Compose** integration and optimization for local development
* **Production ready** Python web server using Nginx and uWSGI
* Python **Flask** backend with:
  * **[Sentry](https://sentry.io/)**: Tracks errors in all major languages & frameworks
  * **[ApiDoc](https://apidocjs.com/)**: Swagger live documentation generation
  * **[Marshmallow](https://marshmallow.readthedocs.io/en/latest/)**: model and data serialization (convert model objects to JSON)
  * **[Webargs](https://webargs.readthedocs.io/en/latest/index.html)**: parse, validate and document inputs to the endpoint / route
  * **[passlib](https://passlib.readthedocs.io/en/stable/)**: hashing
  * **[JWT token](https://flask-jwt-extended.readthedocs.io/en/stable/)** authentication
  * **[SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)** models (independent of Flask extensions, so they can be used with Celery workers directly)
  * Basic starting models for users and groups (modify and remove as you need)
  * **[Alembic](https://alembic.sqlalchemy.org/en/latest/index.html)** migrations
  * **[CORS](https://flask-cors.readthedocs.io/en/latest/index.html)** (Cross Origin Resource Sharing)
  * **[requests](https://github.com/psf/requests)** (send http request)
* REST backend tests based on **[Pytest](https://docs.pytest.org/en/6.2.x/)**, integrated with Docker, so you can test the full API interaction, independent on the database. As it runs in Docker, it can build a new data store from scratch each time (so you can use ElasticSearch, MongoDB, CouchDB, or whatever you want, and just test that the API works)
* Easy Python integration with **[Jupyter Kernels](https://jupyter.org/)** for remote or in-Docker development