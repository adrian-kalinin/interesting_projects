# Interesting Projects API

There are APIs for Project Entries, Webhook Configs and Authentication. All endpoints are documented with Swagger, so there is not much need to explain more here.

Authentication is done with a token in Authorization request header (e.g. `Authorization: Token foobar`). 

## Schema

The schema of the project is avaiable at http://127.0.0.1:8000/openapi-schema/, and there is also Swagger at http://127.0.0.1:8000/swagger/ (login to view all endpoints).

## Requirements

- Python 3.8+
- Docker
- docker-compose

## How to launch

1. Clone the repository (e.g. `git clone https://github.com/adrian-kalinin/interesting_projects`).
2. Create `.env` file with environment variables in directory `interesting_projects/` based on `interesting_projects/.template.env`.
3. Make sure Docker is running on your machine and run `docker-compose up`.