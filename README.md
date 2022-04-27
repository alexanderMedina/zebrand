# Zebrand
## API Documentation

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Catalog application shows multiple products

## Features

- Crud User Operations
- Crud Catalog Operations

## Tech

The APP uses a number of open source projects to work properly:

- [FastaApi] - Python Framework
- [Python] - Language
- [Alembic] - Migration Controller
- [Docker] - Containerization
- [Elastic Stack] - For Log and Analyze
- [SQLALCHEMY] - ORM
- [AWS SES] - For notifications

## Installation

Application requires [Docker and Docker compose](https://www.docker.com/)

First change the .env.example name to .env after that :

Build the container

```sh
docker-compose build --no-cache
```

Start Container

```sh
docker-compose up -d
```

## API Documentation

If you want to visualize api documentation use the postman collection inside the project or go to :

```sh 
http://localhost:8000/docs
```

# Use

The first time the application runs is going to create a user with this credentials (that you can use to log in):
```sh 
{
    "email": "admin@admin.com",
    "password":"Qwerty123"
}
```

To visualize the Log that shows what products the anonymous users just saw go to :

username: elastic
password: changeme
```sh 
http://localhost:5601/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2022-03-28T15:52:20.224Z',to:now))&_a=(columns:!(),filters:!(),index:'logs-*',interval:auto,query:(language:kuery,query:''),sort:!(!('@timestamp',desc)))
```

# Architecture

The application is using a ddd approach with a hexagonal architecture 

![alt text](https://sevenpeakssoftware.com/wp-content/uploads/2020/12/Hexagonal-1.png)

also we are following this classic rules in the directories and dependencies:

![alt text](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/media/ddd-oriented-microservice/domain-driven-design-microservice.png)

in the future will be much easier migrate from this monolithic projecto into a microservices one.

## License

MIT
