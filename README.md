Ubiwhere - Docker Django Postgis
=============
Ubiwhere - A REST API that allows the management of occurrences in an urban environment.
## Version Control

Stack and version numbers used:

| Name           | Version  | 
|----------------|----------|
| Python         | 3.8.0    |
| Django         | 1.11.29  |
| Postgresql (psql)           | 10.7     |
| Docker         | 20.10.6  |
| Docker Compose | 1.29.0   |
| Postgresql     | 11.1     |

see more in `requirements.txt`

## Folder structure

```
$ tree -L 1 --dirsfirst

.
├── api                 # api files - occurences
├── auth                # authentication files - register, get token from login
├── core                # actual webapp core
├── Dockerfile          # docker commands
├── README.md           # this file
├── docker-compose.yml  # docker specification
├── manage.py           # administrative tasks
└── requirements.txt    # project requirements

```

## Setting up

### Docker
See installation instructions at: [docker documentation](https://docs.docker.com/install/)
### Docker Compose
Install [docker compose](https://github.com/docker/compose), see installation
instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

### Django
Django is installed through the requirements 

Edit the `core/settings.py`and `docker-compose.yml` file with the correct database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgis',
        'PORT': 5432,
    }
}
```
## Fire it up
Clone repository by issuing the following command:
```bash
$ git clone https://github.com/DansMarquis/Ubiwhere.git
```
Start the container by issuing one of the following commands:
```bash
$ docker-compose up             # run in foreground
OR
$ docker-compose up -d          # run in background
```
Run migrations by issuing the following commands:
```bash
$ docker exec -it django bash   # open docker bash
$ python manage.py migrate      # apply migrations
```
Create a Super User (admin account) by issuing the following commands:
```bash
$ docker exec -it django bash       # open docker bash
$ python manage.py createsuperuser  # create super user
```
```bash
#Example:

Username: admin
Email address: admin@example.com
Password: admin
Password (again): admin
Superuser created successfully.
```
Connect to docker database image postgis by issuing the following commands:
```bash
docker exec -it postgis psql -U postgres
\c postgres
\d
$ docker exec -it postgis psql -U postgres # open postgresql bash
$$ \c postgres                             # connected to database "postgres" as user "postgres"
$$ \d                                      #check database relations and tables
```
Now you can access the application at <http://127.0.0.1:8000> and the admin site
at <http://127.0.0.1:8000/admin>.

If app is waiting for connection run `$ docker-compose up` again.
## Other commands
Build images:
```bash
$ docker-compose build
$ docker-compose build --no-cache       # build without cache
```

See processes:
```bash
$ docker-compose ps                 # docker-compose processes
$ docker ps -a                      # docker processes (sometimes needed)
$ docker stats [container name]     # see live docker container metrics
```

See logs:
```bash
# See logs of all services
$ docker-compose logs

# See logs of a specific service
$ docker-compose logs -f [service_name]
```

## Endpoints
Context | Endpoint
------------ | -------------
Admin Dashboard | <http://127.0.0.1:8000/admin/>
User Account Registration | <http://127.0.0.1:8000/auth/register/>
User Account Login | <http://127.0.0.1:8000/api-authlogin/>
User Account Login (get token) | <http://127.0.0.1:8000/auth/login/>
Occurences List - filters by Author and Category| <http://127.0.0.1:8000/occurrences/>
Occurence Detail | <http://127.0.0.1:8000/occurrences/{id}>
Occurence Search by Radius - Ubiwhere center point and 8km radius by default| <http://127.0.0.1:8000/searchRadius/>

Being a new User, in Occurrences `POST`, some fields have been omitted (read only) since only the Description, Location and Category can be changed. The other fields are fill by default. 

Example of `Location` Field Fill as a User:
```
SRID=4326;POINT (-9.404296873690489 11.60919340634501)
```
An Admin (in Admin Dashboard) can pick the `Location` from the Map.

I left commented in the admistrator part the fields that should be read-only, that is, you could only change the `State` of the occurrence.



