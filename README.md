# What is it

This is skeleton for Django project using Docker Compose

Project consists of several services:
1. Django app
2. Celery (asynchronous task queue)
3. Celery beat
4. Database (Postgres)
5. Broker for celery (Rabbitmq)
6. Cache (Redis)
7. Proxy server (Nginx)

Containers turned off by default:
1. Adminer (For manual changing db scheme)

## How to boot?

You should have Docker and Docker Compose installed
Change directory to project root and type:
```
docker-compose build
docker-compose up
```
or
```
docker-compose up --build
```

To run as demon (background process) type:
```
docker-compose up --build -d
```

To watch logs:
```
docker-compose logs -f
```

To stop:
```
docker-compose down
```

### Hints
To restart only one or several services:
```
docker-compose stop [<service_name>...] && docker-compose start [<service_name>...]
```

To switch to the interactive mode
```
docker-compose exec <service_name> <shell_name (e.g. bash or sh)>
```
## Making migrations

Switch to the interactive mode
```
docker-compose exec app bash
```

And then:

```
./manage.py makemigrations [APPS...]
```

Then quit
```
exit
```
If you running on Linux, the files created by ```django-admin``` in container owned by ```root```
Change the ownership of new files
```
sudo chown -R $USER:$USER app/
```

## Production mode
Optionally create ```git branch``` called e.g. ```release```
Change dev settings in env files to prod settings
And deploy only this branch (Merge ```master``` to it)
