<h1 align="center"> To_do_do </h1> <br>

<p align="center">
  Simple to_do application on Django
</p>


## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Quick Start](#quick-start)

## Introduction

This simple web application on Python for creating to_do is made using the Django framework. Access to  your personal page is provided after registration. All users and their to_do lists are stored in SQLite.


## Requirements
The application can be run locally or in a docker container, the requirements for each setup are listed below.

### Local
* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Django 3.2.6](https://docs.djangoproject.com/en/3.2/releases/3.2.6/)

### Docker
* [Docker](https://www.docker.com/get-docker)


## Quick Start

### Run Local

Run application
```bash
$ python manage.py runserver 0.0.0.0:8000 
```
Application will run by default on port `8000`. Of course, you can change it, if you want.
### Run Docker

First build the image:
```bash
$ docker build -t todo.
```

When ready, run it:
```bash
$ docker run -p 8000:8000 todo
```

Application will run by default on port `8000`
