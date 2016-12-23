# Councilmatic Starter Template
This repo provides starter code and documentation for new Councilmatic instances.

## About Councilmatic

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on city representatives and their legislative activity.

Councilmatic started as a Code for America project by Mjumbe Poe, who designed the earliest version of a Councilmatic site for [Philadelphia](http://philly.councilmatic.org/). DataMade then implemented Councilmatic in New York City (in partnership with the Participatory Politics Foundation), Chicago (in partnership with the Sunlight foundation), and Los Angeles (in partnership with the Los Angeles County Metropolitan Transportation Authority).

To simplify redeployment of Councilmatic instances, DataMade identified two necessities: (1) Open Civic Data, a data standard for describing people, organizations, events, and bills, and (2) the abstraciton of core functionality into a separate app. DataMade thus built `django-councilmatic` – a django app with base functionality, common across all cities, which implements the OCD data standard.

Use this template to create a councilmatic app for a new city - analogous to DataMade projects, such as NYC Councimatic & Chicago Councilmatic.

## Get started

NOTE: This guide focuses on setting up your app for development. It does not discuss in detail the process of finding, scraping, and importing city data or deploying your site.

### Get data

You need data about your city in the Open Civic Data API.

How you get your data into an instance of the OCD API is up to you. What does DataMade do? We use scrapers, which run nightly to update the API by scraping the data from Legistar-backed sites operated by NYC, Chicago, and LA Metro. Your city may be running a Legistar-backed site, and if so, you can checkout [`python-legistar-scraper`](https://github.com/opencivicdata/python-legistar-scraper) and the [`pupa`](https://github.com/opencivicdata/pupa) framework to get a head start on scraping those sites.

If you need examples of how to customize your scraper, look at [`scrapers-us-municipal`](https://github.com/opencivicdata/scrapers-us-municipal)) as well as [DataMade](https://datamade.us/), which hosts several municipal-level scrapers. You can find information about what cities and other governmental bodies are already covered at [`http://ocd.datamade.us/jurisdictions/`](http://ocd.datamade.us/jurisdictions/).

### Create your site

1. **Install OS Level dependencies**

* Python 3.4
* PostgreSQL 9.4 +

2. **Clone this project and make it your own**
```
git clone https://github.com/datamade/councilmatic-starter-template.git yourcity_councilmatic
```

3. **Make a virtualenv and install dependencies**

We recommend using [virtualenv](https://virtualenv.readthedocs.io/en/latest/)
and
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
for working in a virtualized development environment. [Read how to set up
virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once you have virtualenvwrapper set up, do the following in your bash profile:

```bash
mkvirtualenv councilmatic
cd yourcity_councilmatic
pip install -r requirements.txt
```

4. **Rename the "city" app**

Inside the git repository that you cloned above, you should see a folder called `city`. Rename that to something that makes sense for your project, e.g., "chicago."

```bash
mv city chicago
```

Now, update the main settings file - `councilmatic/settings.py`. First, add the new name of the folder that you just changed to INSTALLED_APPS.

```python
INSTALLED_APPS = (
    ...
    ~'city',~
    'chicago',
)
```

Then, change the TIME_ZONE. You can use [this list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to find the correct formatting.

```python
TIME_ZONE = 'America/Chicago'
```

5. **update city-specific settings**

In the `councilmatic` folder you'll find a settings file called `settings_jursidiction.py`. These settings tell your Councilmatic instance how to populate different parts of the UI and get fresh data from the OCD API.

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
            <td>OCD_JURISDICTION_ID</td>
            <td>
                <p>For scrapers hosted on the Datamade OCD API, you can
                find the jurisdiction id <a href="http://ocd.datamade.us/jurisdictions/">here</a>.</p>

                <p>Otherwise, look at the <code>/jurisdictions/</code> endpoint of the <a href="https://github.com/opencivicdata/api.opencivicdata.org">OCD API</a>.</p>
            </td>
            <td>ocd-jurisdiction/country:us/state:il/place:chicago/government</td>
            <td>No</td>
        </tr>
        <tr>
            <td>OCD_CITY_COUNCIL_ID</td>
            <td>
                <p>Set either <code>OCD_CITY_COUNCIL_ID</code> or <code>OCD_CITY_COUNCIL_NAME</code> - this
                identifies your city council.</p>

                <p><code>OCD_CITY_COUNCIL_ID</code> will take precedence over<code>OCD_CITY_COUNCIL_NAME</code>. But if your OCD IDs are not persistent, it may make more sense to set <code>OCD_CITY_COUNCIL_NAME</code>.</p>

                <p>You can find the name and id of your city council on the <a href="http://ocd.datamade.us/organizations/?jurisdiction_id=YOUR_JURISDICTION_ID">Datamade OCD API</a> or by using the same path to your own OCD API.</p>
            </td>
            <td>ocd-organization/ef168607-9135-4177-ad8e-c1f7a4806c3a</td>
            <td>Only if you set OCD_CITY_COUNCIL_NAME</td>
        </tr>
        <tr>
            <td>OCD_CITY_COUNCIL_NAME</td>
            <td>
                See OCD_CITY_COUNCIL_ID
            </td>
            <td>Chicago City Government</td>
            <td>Only if you set OCD_CITY_COUNCIL_ID</td>
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
                data for in your OCD API.
            </td>
            <td>['2007', '2011', '2015']</td>
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

4. **update deployment settings**

In the `councilmatic` folder you'll find another settings file called `settings_deployment.py.example`. Make a copy of it so that you can customize it for your city:

```
cp councilmatic/settings_deployment.py.example councilmatic/settings_deployment.py
```

This file is important! It's where you keep parts of your Councilmatic that you should end up in version control (e.g., passwords, database connection strings, etc., which will vary based on where the app is running and which you probably won't want other people to know). Most of these variables are generic Django settings, which you can look up in the [Django docs](https://docs.djangoproject.com/en/1.10/ref/settings/); this table shows only the variables that you need to customize.

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
                Used by the <a href="https://github.com/datamade/django-councilmatic/blob/master/councilmatic_core/views.py#L426-L434">`flush` view</a>in `django-councilmatic` to clear Django's cache.
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

5. **set up your database**
  :speech_balloon:

6. **import data**
  :speech_balloon:

7. **run the app!**
  :speech_balloon:

