# councilmatic-starter-template
starter code &amp; documentation for new councilmatic instances

:warning: STATUS: currently in development :warning:  
:speech_balloon: parts of the documentation that aren't fully fleshed out are marked with a speech balloon - if you have questions, do pester us to elaborate & finish the content

## Some context: a high level overview

The [councilmatic family](https://www.councilmatic.org/) is a set of web apps for keeping tabs on local city councils. This template is for creating a councilmatic app for a new city.

Councilmatic started as a Code for America project by Mjumbe Poe, for the city of Philadelphia. DataMade then implemented councilmatic in New York City (in partnership with the Participatory Politics Foundation) & Chicago (in partnership with the Sunlight foundation).

NYC Councilmatic & Chicago Councilmatic are built on `django-councilmatic` (a django app with core functionality that is common across all cities) & open civic data (a data standard for describing people, organizations, events and bills). Using a data standard & abstracting out the core functionality ultimately makes councilmatic much easier to re-deploy. This template is for building a councilmatic app on top of `django-councilmatic` & the OCD API - analogous to NYC Councimatic & Chicago Councilmatic.

To use this template, you'll need to have your city's data in the open civic data api. :speech_balloon:

## Quick start guide

NOTE: This is not a comprehensive overview of how to customize councilmatic :speech_balloon: or how to deploy a live site :speech_balloon: - only a guide to getting an app set up locally for development.

1. **fork this code**  
  :speech_balloon:

2. **install stuff**  
  :speech_balloon:  

3. **update city-specific settings**  
  :speech_balloon:  

4. **update deployment settings**  
  :speech_balloon:  

5. **set up your database**  
  :speech_balloon:

6. **import data**  
  :speech_balloon:

7. **run the app!**  
  :speech_balloon:

