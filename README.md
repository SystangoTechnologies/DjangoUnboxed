
## NinDjango

With collaborative efforts from the CTO office, we have prepared this Django Boilerplate. This boilerplate is aimed to be generic in a way that it solves most of the common problems that are faced in development process, specific to Python-Django development. Moreover it also has the best practices followed in web app development catering the microservice architecture.

## Technology

 - Django 1.11  LTS
 - Django Rest Framework 
 - Fully Dockerised Setup (configuration driven)
 - Smart Logging (DB, Requests)
 - Elastic Solutions    (FileBeat, MetricBeat and HeartBeat) 
 - Celery
 - Rabbit MQ
 - JWT
 - Unit tests
 - Swagger
 
 ## Description
 - ***Django*** :- We have opted for Django, as we wanted to have a strong
   framework and complete ORM solution since we are planning to go with
   Python and with SQL based database
 - ***Django Rest Framework*** :- We opted for DRF as this is the best
   solution available for REST APIs for Python.
 - ***Fully Dockerised Setup*** :- Docker has become an integral part of the
   setup these days. All the settings are yml driven and are
   configurable as per the business need. One can easily turn off/on
   configurations/services via this.
 - ***Smart Logging and EK*** :- We have integrated customized logger
   interface, tracking DB Logs, Request Logs and App Logs with our own
   hand tailored logger implementation that enables us to predict from
   the logs if the application is going to face issues/problems.
   Moreover we have integrated the EK stack in this that enables us to
   harness great analytical and searching tool Kibana. Basically the
   boilerplate is designed to transfer all the logs on Kibana, this is
   happening via Filebeat. All the logs can then be queried and
   analytics can be drawn from them.
 - ***System Monitoring*** :- We have included integration of MetricBeat and
   HeartBeat, they are efficient solutions to monitor system levels and
   vitals.
 - ***Celery*** :- The most preferred delayed task runner when handling
   asynchronous tasks with django applications. Very robust & easy to
   integrate.
 - ***Rabbit MQ*** :- When working with microservices, the quintessential
   requirement is of inter service communication, this where message
   broker comes into picture. Since we need to avoid the synchronous
   dependencies of the REST communication. Hence we have provisioned
   dedicated pub/sub configurations that constantly monitor the Rabbit
   MQ and execute tasks in asynchronous way.
 - ***JWT*** :- The reason why we selected JWT is that, it is used is to prove
   that the sent data was actually created by an authentic source and
   this is the most widely used mechanism while communication is
   happening over REST APIs.
 - ***Unit Test*** :- We have included the unit tests in such a way that the
   APIs are stubbed and there is no incorporation of Databases, thus
   avoiding the overheads related with Databases. Since we aim to have
   pure unit tests hence we have provisioned stubbed methods for unit
   tests.
 - ***Swagger*** :- Though for REST APIs we can get a good document available
   via Django REST Framework, but that is limited in some ways like
   publishing. We selected swagger, so that APIs can be published and be
   tested externally.

## Application Structure

```
|____boilerplate
| |____config
|____boilerplate_app
| |____migrations
|____compose
|____publisher_subscriber
|____requirements
```
## Running the server locally

 * Clone this repo
 * Install python3.6
 * Intall dependencies:
> pip install -r requirements.txt
 * Run the server:
> python manage.py runserver
 * Install [docker compose](https://docs.docker.com/compose/install/)
 * Run docker:
> docker-compose build

> docker-compose up
 * To check the server, open `http://localhost:8000/`

## Contributors
Rishabh Shah

## License

This project is licensed under the terms of the MIT license.
