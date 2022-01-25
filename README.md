# invodata

# Docker Helper

https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

# Create .env File in your root project directory with following content

    POSTGRES_NAME=<postgres>
    POSTGRES_USER=<postgres>
    POSTGRES_PASSWORD=<postgres>
    POSTGRES_HOST=<postgres>
    EMAIL_HOST=<smtp.gmail.com>
    EMAIL_HOST_USER=<email>
    EMAIL_HOST_PASSWORD=<password>

# Migrate

    docker-compose -f docker-compose.yml run --rm django python manage.py migrate

# Migrations

    docker-compose -f docker-compose.yml run --rm django python manage.py makemigrations

# Create Super User

    docker-compose -f docker-compose.yml run --rm django python manage.py createsuperuser

# Shell

    docker-compose -f docker-compose.yml run --rm django python manage.py shell

# Build

    docker-compose build

# Running or Up

     docker-compose up -d




