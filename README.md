# moe_count_django

Reborn Moe Count, now written in Django with Celery and deployed with Gunicorn and Nginx!

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

