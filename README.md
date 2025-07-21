# Councilmatic Starter Template (Updated)

This repo provides updated starter code and documentation for new Councilmatic instances, incorporating modern Django development patterns and tooling.

## About Councilmatic

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on city representatives and their legislative activity.

Councilmatic started as a Code for America project by Mjumbe Poe, who designed the earliest version of a Councilmatic site – [Councilmatic Philadelphia](http://philly.councilmatic.org/). DataMade then implemented Councilmatic in New York City, Chicago, and Los Angeles.

This template uses `django-councilmatic` – [a Django app](https://github.com/datamade/django-councilmatic) with base functionality common across all cities, which implements the Open Civic Data standard.

## Features

- **Modern Django 4.2+** with updated patterns and security
- **Docker-based development** environment
- **Node.js + Webpack** for frontend asset building
- **Bootstrap 5** with customizable SCSS
- **PostgreSQL + PostGIS** for geospatial data
- **Elasticserch** for full-text search
- **GitHub Actions** for CI/CD
- **Accessibility** features built-in

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)

### 1. Clone and Setup

```bash
git clone https://github.com/datamade/councilmatic-starter-template.git yourcity_councilmatic
cd yourcity_councilmatic
cp .env.example .env
```

### 2. Configure Your Instance

**`.env`** - Set your environment variables:
- Generate a secure `DJANGO_SECRET_KEY`
- Configure your database connection
- Set up search engine URLs

### 3. Initial Setup

```bash
docker compose build
```

### 4. Create a Superuser

```bash
docker compose run --rm app python manage.py createsuperuser
```

### 5. Start Development Server

```bash
docker compose up
```

Visit http://localhost:8000 to see your site!

## Development Workflow

### Frontend Development

The template uses Webpack to build frontend assets:

- **SCSS files**: `yourcity/static/scss/`
- **JavaScript files**: `yourcity/static/js/`

Customize your city's branding by editing:
- `yourcity/static/scss/main.scss` - Colors, fonts, and styles
- `yourcity/static/js/main.js` - JavaScript functionality

## Data Import

To import legislative data, you'll need to:

1. **Install pupa**: Follow the [pupa documentation](https://open-civic-data.readthedocs.io/en/latest/scrape/index.html)
2. **Create scrapers** for your city's data sources
3. **Run import**: Use pupa to import into your database

Example workflow:
```bash
# Install pupa in your environment
pip install pupa

# Create and run scrapers (example)
pupa update your_city_scraper

# Update search index
python manage.py rebuild_index
```

## Customization

### Templates

Councilmatic gives you the infrastructure. You create the interface! Build your site by
adding templates to `yourcity/templates/`. 

### Models

Extend core models in `yourcity/models.py`:
```python
class YourCityBill(Bill):
    # Add custom fields or methods
    custom_field = models.CharField(max_length=100, blank=True)
    
    class Meta:
        proxy = True
```

## Getting Help

- [Councilmatic documentation](https://www.councilmatic.org/)
- [Django Councilmatic GitHub](https://github.com/datamade/django-councilmatic)
- [Open Civic Data documentation](https://opencivicdata.readthedocs.io/)

## License

Copyright (c) 2025 Participatory Politics Foundation and DataMade. Released under the [MIT License](LICENSE).
