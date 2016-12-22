# councilmatic-starter-template
This repo provides starter code &amp; documentation for new councilmatic instances.

## About Councilmatic

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on city representatives and their legislative activity.

Councilmatic started as a Code for America project by Mjumbe Poe, who designed the earliest version of a Councilmatic site for [Philadelphia](http://philly.councilmatic.org/). DataMade then implemented Councilmatic in New York City (in partnership with the Participatory Politics Foundation), Chicago (in partnership with the Sunlight foundation), and Los Angeles (in partnership with the Los Angeles County Metropolitan Transportation Authority).

DataMade built `django-councilmatic` – a django app with core functionality, common across all cities, which implements Open Civic Data (a data standard for describing people, organizations, events, and bills). The OCD data standard and the abstraciton of core functionality into a separate app simplifies the creation of Councilmatic sites.

Use this template to create a councilmatic app for a new city - analogous to DataMade projects, such as NYC Councimatic & Chicago Councilmatic.

## Get started

NOTE: This guide focuses on setting up your app for development. It does not discuss in detail the process of finding, scraping, and importing city data or deploying your site.

### Import data

You need data to build a Councilmatic instance. To do so, you should check that your city's data lives in the Open Civic Data API. Then, you need to write a scraper and an import script for loading data about people, legislation, events, etc. Much of what you need can be found in the [Open Civic Data documentation](https://opencivicdata.readthedocs.io/en/latest/).

### Create your site
:speech_balloon:

2. **fork this code**
  :speech_balloon:

2. **install stuff**
  :speech_balloon:

3. **update city-specific settings**
  - set your `OCD_JURISDICTION_ID`.
    you can find the jurisdiction ids at http://ocd.datamade.us/jurisdictions/
  - set either `OCD_CITY_COUNCIL_ID` or `OCD_CITY_COUNCIL_NAME` - this identifies your city council
    `OCD_CITY_COUNCIL_ID` will take precedence over `OCD_CITY_COUNCIL_NAME`, but it may make more sense to set `OCD_CITY_COUNCIL_NAME` if your OCD IDs aren't persistent. You can find the name and id of your city council at http://ocd.datamade.us/organizations/?jurisdiction_id=YOUR_JURISDICTION_ID
  - :speech_balloon:

4. **update deployment settings**
  :speech_balloon:

5. **set up your database**
  :speech_balloon:

6. **import data**
  :speech_balloon:

7. **run the app!**
  :speech_balloon:





To use this template, you'll need to have your city's data in the Open Civic
Data API. How you get your data into an instance of the OCD API is up to you.
In the case of New York City and Chicago, there are scrapers which run nightly
to update the API by scraping the data from the Legistar backed sites operated
by those cities. If the city that you are interested in building a Councilmatic
instance for happens to be running a Legistar backed site, checkout
[`python-legistar-scraper`](https://github.com/opencivicdata/python-legistar-scraper)
and the [`pupa`](https://github.com/opencivicdata/pupa) framework to get a head
start on scraping those sites (for examples of how to customize your scraper,
look at
[`scrapers-us-municipal`](https://github.com/opencivicdata/scrapers-us-municipal)).
[DataMade](https://datamade.us/) hosts several municipal level scrapers.
Information about what cities and other governmental bodies are already covered
can be seen at
[`http://ocd.datamade.us/jurisdictions/`](http://ocd.datamade.us/jurisdictions/).

## Quick start guide

NOTE: This is not yet a comprehensive overview of how to customize councilmatic
:speech_balloon: or how to deploy a live site :speech_balloon:.

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

Once you have virtualenvwrapper set up,

```
mkvirtualenv councilmatic
cd yourcity_councilmatic
pip install -r requirements.txt
```

4. **Rename app**

Inside the git repository that you cloned above, you should see a
folder called `yourcity`. Rename that to something that makes sense
for you:

```
mv yourcity chicago
```

Now make sure that you update the main `settings.py` file for the
project inside the `councilmatic` folder:

```
# Find the INSTALLED_APPS list and change 'yourcity' to whatever you
# named it above ('chicago' in the example)

INSTALLED_APPS = (
    ...
    ~'yourcity',~
    'chicago',
)
```

4. **update city-specific settings**

In the `councilmatic` folder you'll find a settings file called
`settings_jursidiction.py`.These are all the jurisdiction specific settings that will tell your
Councilmatic instance how to populate different parts of the UI and get fresh
data from the OCD API. :speech_balloon:

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
            <td>`OCD_JURISDICTION_ID`</td>
            <td>
                If your city's scraper is hosted on the Datamade OCD API, you can
                find it's jurisdiction id at
                [http://ocd.datamade.us/jurisdictions/](http://ocd.datamade.us/jurisdictions/).
                Otherwise, look at the `/jurisdictions/` endpoint of the [OCD
                API](https://github.com/opencivicdata/api.opencivicdata.org) where
                your data is hosted.
            </td>
            <td>ocd-jurisdiction/country:us/state:il/place:chicago/government</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`OCD_CITY_COUNCIL_ID`</td>
            <td>
                Set either `OCD_CITY_COUNCIL_ID` or `OCD_CITY_COUNCIL_NAME` - this
                identifies your city council `OCD_CITY_COUNCIL_ID` will take precedence over
                `OCD_CITY_COUNCIL_NAME`, but it may make more sense to set
                `OCD_CITY_COUNCIL_NAME` if your OCD IDs aren't persistent. You can find the
                name and id of your city council on the Datamade OCD API at
                http://ocd.datamade.us/organizations/?jurisdiction_id=YOUR_JURISDICTION_ID
                (or using the same path on your own OCD API)
            </td>
            <td>ocd-organization/ef168607-9135-4177-ad8e-c1f7a4806c3a</td>
            <td>Only if `OCD_CITY_COUNCIL_NAME` is set</td>
        </tr>
        <tr>
            <td>`OCD_CITY_COUNCIL_NAME`</td>
            <td>
                See `OCD_CITY_COUNCIL_ID`
            </td>
            <td>Chicago City Government</td>
            <td>Only if `OCD_CITY_COUNCIL_ID` is set</td>
        </tr>
        <tr>
            <td>`CITY_COUNCIL_NAME`</td>
            <td>
                Display name for the legislative body you'll be tracking.
            </td>
            <td>Chicago City Council</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`LEGISLATIVE_SESSIONS`</td>
            <td>
                A list of years that tells Councilmiatic when a new
                body is elected and which of these sessions you have
                data for in your OCD API.
            </td>
            <td>['2007', '2011', '2015']</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_NAME`</td>
            <td>
                Complete, pretty name of the jurisdiction
            </td>
            <td>New York City</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_NAME_SHORT`</td>
            <td>
                Shortened version of the jurisdiction name
            </td>
            <td>NYC</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB`</td>
            <td>
                A dictionary telling Councilmatic how to refer to
                different entities in the jurisdiction
            </td>
            <td>(See individual values below)</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB['MUNICIPAL_DISTRICT']`</td>
            <td>
                The name of a district into which the jurisdiction is divided
            </td>
            <td>Ward</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB['SOURCE']`</td>
            <td>
                The name of the entity responsible for the source data
                that your Councilmatic will be based upon.
            </td>
            <td>Chicago City Clerk</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB['COUNCIL_MEMBER']`</td>
            <td>
                The name of a member of the legislative body your Councilmatic is tracking.
            </td>
            <td>Alderman</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB['COUNCIL_MEMBERS']`</td>
            <td>
                Plural form of the name of a member of the legislative body your Councilmatic is tracking.
            </td>
            <td>Aldermen</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`CITY_VOCAB['EVENTS']`</td>
            <td>
                The name of the meetings that members of the legislative body attend.
            </td>
            <td>Meetings</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`APP_NAME`</td>
            <td>
                The name of the folder where your jurisdiction
                specific code lives.
            </td>
            <td>chicago</td>
            <td>No</td>
        </tr>
        <tr>
            <td>`SITE_META`</td>
            <td>
                Dictionary containing values used in `meta` tags.
            </td>
            <td>(See individual values below)</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['site_name']`</td>
            <td>
                Used for the `og:name`, `og:title`, and `twitter:title` meta tags
            </td>
            <td>Chicago Councilmatic</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['site_desc']`</td>
            <td>
                Used for the `description`, `og:description`, and `twitter:description` meta tags
            </td>
            <td>City Council, demystified. Keep tabs on Chicago legislation, aldermen, & meetings.</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['site_author']`</td>
            <td>
                Used for the `author` meta tag
            </td>
            <td>DataMade</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['site_url']`</td>
            <td>
                Used to build absolute URLs for the meta tags.
            </td>
            <td>https://chicago.councilmatic.org</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['twitter_site']`</td>
            <td>
                Used for `twitter:site` meta tag.
            </td>
            <td>@councilmatic</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`SITE_META['twitter_creator']`</td>
            <td>
                Used for `twitter:creator` meta tag.
            </td>
            <td>@DataMadeCo</td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

4. **update deployment settings**

In the `councilmatic` folder you'll find another settings file called
`settings_deployment.py.example`. Make a copy of it so that you can
customize it for your city:

```
cp councilmatic/settings_deployment.py.example councilmatic/settings_deployment.py
```

This is where you'll keep the parts of your Councilmatic that you
don't want to place into version control (things like passwords,
database connection strings, etc that will vary based on where
the app is running and which you probably won't want other people to
know). Most of them are generic Django settings which you can look up
in the [Django
docs](https://docs.djangoproject.com/en/1.10/ref/settings/). The ones
that aren't are:

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
            <td>`HAYSTACK_CONNECTIONS`</td>
            <td>
                Dictionary of connections used by Haystack. More on
                that
                [here](http://django-haystack.readthedocs.io/en/v2.5.0/tutorial.html#modify-your-settings-py)
            </td>
            <td>No</td>
        </tr>
        <tr>
            <td>`FLUSH_KEY`</td>
            <td>
                Used by the [`flush`
                view](https://github.com/datamade/django-councilmatic/blob/master/councilmatic_core/views.py#L426-L434)
                in `django-councilmatic` to clear Django's cache.
            </td>
            <td>No</td>
        </tr>
        <tr>
            <td>`DISQUS_SHORTNAME`</td>
            <td>
                Will cause Disqus comment threads to be attached to
                individual bill pages.
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`ANALYTICS_TRACKING_CODE`</td>
            <td>
                Google Analytics property ID
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`HEADSHOT_PATH`</td>
            <td>
                Absolute path to where the data loader will save
                images of members of the legislative body that are
                often available through Legistar.
            </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>`EXTRA_APPS`</td>
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

