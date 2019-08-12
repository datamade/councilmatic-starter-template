# Councilmatic Starter Template
This repo provides starter code and documentation for new Councilmatic instances.

## About Councilmatic

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on city representatives and their legislative activity.

Councilmatic started as a Code for America project by Mjumbe Poe, who designed the earliest version of a Councilmatic site – [Councilmatic Philadelphia](http://philly.councilmatic.org/). DataMade then implemented Councilmatic in New York City (in partnership with the Participatory Politics Foundation), Chicago (in partnership with the Sunlight foundation), and Los Angeles (in partnership with the Los Angeles County Metropolitan Transportation Authority).

To simplify redeployment of Councilmatic instances, DataMade identified two necessities: (1) Open Civic Data, a data standard for describing people, organizations, events, and bills, and (2) the abstraciton of core functionality into a separate app. And so, DataMade built `django-councilmatic` – [a django app](https://github.com/datamade/django-councilmatic) with base functionality, common across all cities, which implements the OCD data standard.

With this template, you can create a Councilmatic site for your own city, built using the `django-councilmatic` app. Read on!

## Getting started

### 1. Install OS Level dependencies

* Python 3.4+
* PostgreSQL 9.4+

### 2. Clone this project

```bash
git clone https://github.com/datamade/councilmatic-starter-template.git yourcity_councilmatic
```

### 3. Make a virtualenv and install dependencies

We recommend using [virtualenv](https://virtualenv.readthedocs.io/en/latest/)
and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
for working in a virtualized development environment. [Read how to set up
virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once you have virtualenvwrapper set up, run the following commands in your terminal:

```bash
cd yourcity_councilmatic
mkvirtualenv councilmatic
pip install -r requirements.txt
```

Afterwards, whenever you want to use this virtual environment, run:

```bash
workon yourcity_councilmatic
```

### 4. Set up your database

#### Initialization

Before you can run the website, you need to create a database and install PostGIS.

```bash
createdb yourcity_councilmatic
psql -d yourcity_councilmatic -c "CREATE EXTENSION postgis"
```

Then, run migrations. (Be sure that you are "working on" the correct virtual environment.)

```bash
python manage.py migrate --no-initial-data
```

Finally, create an admin user. Set a username and password when prompted.

```bash
python manage.py createsuperuser
```

#### Find legislative data

`django-councilmatic` leverages, and in some instances, lightly extends the Open Civic Data standard, implemented in Django as [`python-opencivicdata`](https://github.com/opencivicdata/python-opencivicdata). The next step toward running a new Councilmatic instance is to locate data about your city and use it to populate these OCD models.

How you do that is up to you. At DataMade, we maintain a series of external municipal scrapers that retrieve data from Legistar-backed sites.

If your city runs a Legistar-backed site, see [`scrapers-us-municipal`](https://github.com/opencivicdata/scrapers-us-municipal) for several examples of scrapers that will populate a given database with legislative data in the format required by Councilmatic. These scrapers leverage [`python-legistar-scraper`](https://github.com/opencivicdata/python-legistar-scraper) to scrape Legistar and the [`pupa`](https://github.com/opencivicdata/pupa) framework to shape and import data.

If your city does not run a Legistar-backed site, we still recommend using `pupa` as a legislative scraping framework. You can add your scrapers to your Councilmatic repository, or compose them elsewhere.

Next, install and create a settings file for `pupa` –

```bash
pip install pupa
touch pupa_settings.py
```

– and add the following settings:

```python
# Leave these blank
OCD_CITY_COUNCIL_NAME = ''
CITY_COUNCIL_NAME = ''
STATIC_PATH = ''

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'opencivicdata.core.apps.BaseConfig',
    'opencivicdata.legislative.apps.BaseConfig',
    'pupa',
    'councilmatic_core'
)

# Change this if you called your database something different
DATABASE_URL = 'postgres:///yourcity_councilmatic'
```

Finally, initialize `pupa`.

```
pupa dbinit us
pupa init YOUR_CITY_SCRAPER
```

Once you've filled out the prompts, you will see a new directory called `YOUR_CITY_SCRAPER`. Inside, you'll find the scaffolding for the necessary scrapers to populate the database.

Define the `scrape` methods in each of the resulting scraper classes, then run `pupa update YOUR_CITY` to import data. If you aren't sure where to start, [the City Scrapers project](https://github.com/City-Bureau/city-scrapers) includes many examples of scraping all sorts of government websites.

N.b., if you wish to make any changes to the models, see [the `django-councilmatic` README for information on approaches](https://github.com/datamade/django-councilmatic/).

#### Add metadata

`django-councilmatic` comes with management commands to add headshots and geography shapes to `Person` objects and `Post` objects, respectively.

If you've imported people with headshot URLs, run `update_headshots` to download the images and store them where Django knows where to find them.

```bash
python manage.py update_headshots
```

Likewise, if you've imported `Post` objects and you'd like to include geographic boundaries that pertain to them, create a GeoJSON file containing shapes for each division represented in your instance, then run the `import_shapes` command. [See the GeoJSON file in `chi-councilmatic`](https://github.com/datamade/chi-councilmatic/blob/bb33a1ed80623e39df445f5108cfdda5ccfaf942/data/final/shapes/chicago_shapes.json) for an example of the expected format.

```bash
python manage.py import_shapes /path/to/your/shapes.geojson
```

### 5. Rename the "city" app

Now that you have the data, set up your instance.

Inside the git repository that you cloned above, you should see a folder called `city`. Rename this folder to something that makes sense for your project, e.g., "chicago."

```bash
mv city yourcity
```

Now, update the main settings file - `councilmatic/settings.py`. First, in `INSTALLED_APPS`, add the name of the folder that you just renamed:

```python
INSTALLED_APPS = (
    ...
    ~'city',~
    'yourcity',
)
```

Then, change the TIME_ZONE. You can use [this list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to find the correct formatting.

```python
TIME_ZONE = 'America/Chicago'
```

### 6. Update city-specific settings

Look for `councilmatic/settings_jurisdiction.py`. This settings file tells your Councilmatic instance how to populate different parts of the UI and get fresh data from the OCD database. The following table explains why and how to adjust these values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Example value</th>
            <th>Optional?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>OCD_JURISDICTION_IDS</td>
            <td>
                <p>An array of the OCD IDs of jurisdictions covered by your Councilmatic instance. Query the <code>opencivicdata_jurisdictions</code> table for options.</p>
            </td>
            <td>['ocd-jurisdiction/country:us/state:il/place:chicago/government']</td>
            <td>No</td>
        </tr>
        <tr>
            <td>OCD_CITY_COUNCIL_NAME</td>
            <td>
                This identifies the legislative body you'll be tracking. It should correspond to an Organization in your database. Query the <code>opencivicdata_organization</code> table (or <code>opencivicdata.legislative.Organization</code> model in the ORM) for options.
            </td>
            <td>Chicago City Council</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_COUNCIL_NAME</td>
            <td>
                Display name for the legislative body you'll be tracking.
            </td>
            <td>Chicago City Council</td>
            <td>No</td>
        </tr>
        <tr>
            <td>LEGISLATIVE_SESSIONS</td>
            <td>
                A list of years that tells Councilmiatic when a new
                body is elected and which of these sessions you have
                data for in your OCD database.
            </td>
            <td>['2007', '2011', '2015', '2019']</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_NAME</td>
            <td>
                Complete, pretty name of the jurisdiction
            </td>
            <td>New York City</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_NAME_SHORT</td>
            <td>
                Shortened version of the jurisdiction name
            </td>
            <td>NYC</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB</td>
            <td>
                A dictionary telling Councilmatic how to refer to
                different entities in the jurisdiction
            </td>
            <td>(See individual values below)</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB['MUNICIPAL_DISTRICT']</td>
            <td>
                The name of the city sections, which could be a "ward", "sector", "district", etc.
            </td>
            <td>Ward</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB['SOURCE']</td>
            <td>
                The name of the entity responsible for the source data that your Councilmatic will be based upon.
            </td>
            <td>Chicago City Clerk</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB['COUNCIL_MEMBER']</td>
            <td>
                The name of a member of the legislative body that your Councilmatic tracks.
            </td>
            <td>Alderman</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB['COUNCIL_MEMBERS']</td>
            <td>
                Plural form of the name of a member of the legislative body your Councilmatic tracks.
            </td>
            <td>Aldermen</td>
            <td>No</td>
        </tr>
        <tr>
            <td>CITY_VOCAB['EVENTS']</td>
            <td>
                The name of the meetings that members of the legislative body attend.
            </td>
            <td>Meetings</td>
            <td>No</td>
        </tr>
        <tr>
            <td>APP_NAME</td>
            <td>
                The name of the folder where your jurisdiction specific code lives.
            </td>
            <td>chicago</td>
            <td>No</td>
        </tr>
        <tr>
            <td>SITE_META</td>
            <td>
                Dictionary containing values stored in <code>meta</code> tags.
            </td>
            <td>(See individual values below)</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['site_name']</td>
            <td>
                Used for the <code>og:name</code>, <code>og:title</code>, and <code>twitter:title</code> meta tags
            </td>
            <td>Chicago Councilmatic</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['site_desc']</td>
            <td>
                Used for the <code>description</code>, <code>og:description</code>, and <code>twitter:description</code> meta tags
            </td>
            <td>City Council, demystified. Keep tabs on Chicago legislation, aldermen, & meetings.</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['site_author']</td>
            <td>
                Used for the <code>author</code> meta tag
            </td>
            <td>DataMade</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['site_url']</td>
            <td>
                Used to build absolute URLs for the meta tags.
            </td>
            <td>https://chicago.councilmatic.org</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['twitter_site']</td>
            <td>
                Used for <code>twitter:site</code> meta tag.
            </td>
            <td>@councilmatic</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>SITE_META['twitter_creator']</td>
            <td>
                Used for <code>twitter:creator</code>  meta tag.
            </td>
            <td>@DataMadeCo</td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

### 7. Update deployment settings

Look for `councilmatic/settings_deployment.py.example`. Make a copy of it so that you can customize it for your city:

```
cp councilmatic/settings_deployment.py.example councilmatic/settings_deployment.py
```

This file is important! It's where you keep the parts of your Councilmatic that should not end up in version control (e.g., passwords, database connection strings, etc., which will vary based on where the app is running and which you probably won't want other people to know). Most of these variables are generic Django settings, which you can look up in the [Django docs](https://docs.djangoproject.com/en/1.10/ref/settings/); but some of these variables require customization. This table shows only the variables that you need to customize.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Optional?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>HAYSTACK_CONNECTIONS</td>
            <td>
                Dictionary of connections used by Haystack. More on
                that <a href="http://django-haystack.readthedocs.io/en/v2.5.0/tutorial.html#modify-your-settings-py">here</a>.
            </td>
            <td>No</td>
        </tr>
        <tr>
            <td>FLUSH_KEY</td>
            <td>
                Used by the <code>flush</code> view in <code>django-councilmatic</code> to clear Django's cache.
            </td>
            <td>No</td>
        </tr>
        <tr>
            <td>DISQUS_SHORTNAME</td>
            <td>
                Will cause Disqus comment threads to be attached to
                individual bill pages.
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>ANALYTICS_TRACKING_CODE</td>
            <td>
                Google Analytics property ID
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>GOOGLE_API_KEY</td>
            <td>
                API key for rendering maps on council members and person detail pages. <a href="https://developers.google.com/maps/documentation/javascript/get-api-key" target="_blank">Learn about creating your own Google API Key.</a>
            </td>
            <td>No</td>
        </tr>
        <tr>
            <td>HEADSHOT_PATH</td>
            <td>
                Absolute path to where the data loader will save
                images of members of the legislative body that are
                often available through Legistar.
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>EXTRA_APPS</td>
            <td>
                List of additional django apps that you want to use
                with your custom councilmatic
            </td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

### 8. Add a favicon

Get an image (suggested 310x310), and transform it in device-specific favicon images [using this site](http://www.favicomatic.com/). Then, move the images into `<city_app>/static/images/icons`.

### 9. Run Councilmatic locally

Now, you are ready to run your unique version of Councilmatic!

``` bash
python manage.py runserver
```

Navigate to [http://localhost:8000/](http://localhost:8000/).

## Set up search with Haystack and Solr

On a Councilmatic site, users can search bills according to given query parameters. To power our searches, we use [Django Haystack](https://django-haystack.readthedocs.io/en/v2.4.1/toc.html) to connect with [Solr](http://lucene.apache.org/solr/), an open source tool, written in Java.

### Run Solr

Because it's a bit of a heavy dependency, we recommend running a containerized instance of Solr. [See the Solr image in DockerHub](https://hub.docker.com/_/solr/) for more information and startup instructions. Don't forget to update your Haystack config in `councilmatic/settings_deployment.py`, if you map a port other than the Solr default (8983) to your container!

If you prefer to run Solr locally, [see the Solr documentation](https://lucene.apache.org/solr/guide/8_1/solr-tutorial.html#solr-tutorial) for startup instructions.

### Haystack commands to know

[Haystack provides several management commands](https://django-haystack.readthedocs.io/en/v2.4.1/management_commands.html) that make it easy to change and add data to your search index.

To make your data searchable:

```bash
python manage.py rebuild_index
```

If, during the course of development, you need to make changes to the fields that are indexed in `yourcity/search_indexes.py`, you need to regenerate the Solr schema:

```bash
python manage.py build_solr_schema > solr_scripts/schema.xml
```

Remove and recreate your Solr container to capture changes in the Solr schema.

## Errors/Bugs

If something is not behaving intuitively, it is a bug, and should be reported.
Report it [here](https://github.com/datamade/councilmatic-starter-template/issues).

## Note on Patches/Pull Requests

We welcome your ideas and feedback! Here's how to make a contribution:

* Fork the project.
* Make your feature addition or bug fix.
* Commit - please be descriptive, but concise.
* Send a pull request. Bonus points for well-titled topic branches!

## Copyright

Copyright (c) 2019 Participatory Politics Foundation and DataMade. Released under the [MIT License](https://github.com/datamade/councilmatic-starter-template/blob/master/LICENSE).
