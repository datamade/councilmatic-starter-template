# Councilmatic Starter Template

This repo provides starter code and documentation for new Councilmatic instances, incorporating modern Django development patterns and tooling.

## About Councilmatic

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on city representatives and their legislative activity.

Councilmatic started as a Code for America project by Mjumbe Poe, who designed the earliest version of a Councilmatic site – [Councilmatic Philadelphia](http://philly.councilmatic.org/). DataMade then implemented Councilmatic in New York City, Chicago, and Los Angeles.

This template uses `django-councilmatic` – [a Django app](https://github.com/datamade/django-councilmatic) with base functionality common across all cities.

## Features

- **Modern Django 4.2+** with updated patterns and security
- **Docker-based development** environment
- **Node.js + Webpack** for frontend asset building
- **Bootstrap 5** with customizable SCSS
- **PostgreSQL + PostGIS** for geospatial data
- **Elasticserch** for full-text search
- **Accessibility** features built-in

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)

### 1. Create Your Instance

```bash
# Build cookiecutter container 
docker build github.com/datamade/councilmatic-starter-template#master -t cookiecutter:latest

# Generate a new project
docker run -it \
	--mount type=bind,source=$(pwd),target=/cookiecutter \
	cookiecutter gh:datamade/councilmatic-starter-template
```

### 2. Get Customizing!

Consult the README in your new project directory for next steps.
