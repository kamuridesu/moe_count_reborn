# moe_count_django

Reborn Moe Count, now written in Django with Celery and deployed with Gunicorn and Nginx!

# Project Structure

<img src="diagrams/diagram.svg"/>

## Technologies

<!--START_SECTION:stack-->
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

