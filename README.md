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
- **Solr** for full-text search
- **GitHub Actions** for CI/CD
- **Accessibility** features built-in
- **Make commands** for common development tasks

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/) (optional, but recommended)

### 1. Clone and Setup

```bash
git clone https://github.com/datamade/councilmatic-starter-template.git yourcity_councilmatic
cd yourcity_councilmatic
cp .env.example .env
```

### 2. Configure Your City

Edit the following files to customize for your city:

**`yourcity/settings_jurisdiction.py`** - Update all the city-specific settings:
- `OCD_CITY_COUNCIL_NAME`
- `CITY_COUNCIL_NAME` 
- `OCD_JURISDICTION_IDS`
- `CITY_NAME`
- And other vocabulary/branding settings

**`.env`** - Set your environment variables:
- Generate a secure `DJANGO_SECRET_KEY`
- Configure your database connection
- Set up search engine URLs

### 3. Initial Setup

Using Make (recommended):
```bash
make setup
```

Or manually:
```bash
docker compose build
docker compose run --rm app python manage.py migrate
docker compose run --rm app python manage.py collectstatic --noinput
```

### 4. Create a Superuser

```bash
make superuser
# or
docker compose run --rm app python manage.py createsuperuser
```

### 5. Start Development Server

```bash
make run
# or
docker compose up
```

Visit http://localhost:8000 to see your site!

## Development Workflow

### Common Commands

```bash
# Start development server
make run

# Run tests
make test

# Open Django shell
make shell

# Run migrations
make migrate

# Create new migrations
make makemigrations

# Build frontend assets
make build

# Watch and rebuild assets during development
make watch

# Lint code
make lint

# Format code
make format

# View logs
make logs
```

### Frontend Development

The template uses Webpack to build frontend assets:

- **SCSS files**: `yourcity/static/scss/`
- **JavaScript files**: `yourcity/static/js/`
- **Built assets**: Generated to `yourcity/static/dist/`

Customize your city's branding by editing:
- `yourcity/static/scss/main.scss` - Colors, fonts, and styles
- `yourcity/static/js/main.js` - JavaScript functionality

### Setting Up Search

This template uses Solr for search. You'll need to:

1. **Set up Solr** (see Solr documentation)
2. **Configure Haystack** in your settings
3. **Generate schema**: `python manage.py build_solr_schema > solr_scripts/schema.xml`
4. **Build search index**: `python manage.py rebuild_index`

## Data Import

To import legislative data, you'll need to:

1. **Install pupa**: Follow the [pupa documentation](https://opencivicdata.readthedocs.io/en/latest/scraping/)
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

Base templates are in `councilmatic_core`. Override them by creating files with the same name in:
- `templates/councilmatic_core/` - Override core templates
- `templates/yourcity/` - Your city-specific templates

### Models

Extend core models in `yourcity/models.py`:
```python
class YourCityBill(Bill):
    # Add custom fields or methods
    custom_field = models.CharField(max_length=100, blank=True)
    
    class Meta:
        proxy = True
```

### Views

Override core views in `yourcity/views.py`:
```python
from councilmatic_core.views import BillDetailView

class YourCityBillDetailView(BillDetailView):
    # Custom functionality
    pass
```

## Deployment

### Environment Variables

Set these in production:
- `DJANGO_SECRET_KEY` - Generate a secure key
- `DEBUG=False`
- `DJANGO_ALLOWED_HOSTS` - Your domain(s)
- `DATABASE_URL` - Your production database
- `SOLR_URL` - Your Solr instance
- Storage settings (AWS S3, etc.)

### CI/CD

The included GitHub Actions workflow will:
- Run linters (Black, Flake8, ESLint, Prettier)
- Run tests
- Can be extended for deployment

## Contributing

1. Fork the project
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `make test`
5. Run linters: `make lint`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## Getting Help

- [Councilmatic documentation](https://www.councilmatic.org/)
- [Django Councilmatic GitHub](https://github.com/datamade/django-councilmatic)
- [Open Civic Data documentation](https://opencivicdata.readthedocs.io/)

## License

Copyright (c) 2024 Participatory Politics Foundation and DataMade. Released under the [MIT License](LICENSE).
