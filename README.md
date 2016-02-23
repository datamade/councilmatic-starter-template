# councilmatic-starter-template
starter code &amp; documentation for new councilmatic instances

:warning: STATUS: currently in development :warning:

### A high level overview

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on local city councils. This template is for creating a councilmatic app for a new city.

Councilmatic started as a Code for America project by Mjumbe Poe, for the city of Philadelphia. DataMade then implemented councilmatic in New York City (in partnership with the Participatory Politics Foundation) & Chicago (in partnership with the Sunlight foundation).

NYC Councilmatic & Chicago Councilmatic are built on `django-councilmatic`, a django app with core functionality that is common across all cities. Splitting out the core functionality & the city specific customizations makes councilmatic much easier to re-deploy. This template is for building a councilmatic app on top of `django-councilmatic`, analogous to NYC Councimatic & Chicago Councilmatic.
