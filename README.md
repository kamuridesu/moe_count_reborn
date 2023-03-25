# moe_count_django

Reborn Moe Count, now written in Django with Celery and deployed with Gunicorn and Nginx!

This is a Django version of my Flask project, [Moe Count](https://github.com/kamuridesu/moe_count).

# Project Structure

<img src="diagrams/diagram.svg"/>

## Technologies

<!--START_SECTION:stack-->
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
<!--END_SECTION:stack-->

And Celery!

# How to run

## Requirements

This project requires Docker and docker-compose to run.

## Environment
Export the environments variables containing the Django secret:

```sh
export DJANGO_SECRET_KEY=""
```

## Running

Just run the following command:

```sh
docker-compose up -d --build
```

# Endpoints

- `/`:
  - Parameters: `username`. If `username` is empty, it'll raise a 404 page.

## Advantages
- More fine grained control over every step, from the web server to the functions.
- Structure more organized.
## Disaventages
- Bloat. The project has a lot of files.
- Memory hungry: Celery uses about 300M, Django uses about 100M. In total, this project uses almost 500M of RAM, while the Flask one is using something like 50M.
