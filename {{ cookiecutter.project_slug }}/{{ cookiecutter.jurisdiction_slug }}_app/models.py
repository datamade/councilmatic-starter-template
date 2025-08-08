from django.conf import settings
from django.db import models
from councilmatic_core.models import Bill, Event, Person, Organization
from datetime import datetime
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)


class {{ cookiecutter.jurisdiction_camel_case }}Bill(Bill):
    """
    Extend the base Bill model for city-specific functionality.
    Add any custom fields or methods specific to your city here.
    """
    
    class Meta:
        proxy = True

    def __str__(self):
        return self.friendly_name or self.identifier


class {{ cookiecutter.jurisdiction_camel_case }}Event(Event):
    """
    Extend the base Event model for city-specific functionality.
    Add any custom fields or methods specific to your city here.
    """
    
    class Meta:
        proxy = True


class {{ cookiecutter.jurisdiction_camel_case }}Person(Person):
    """
    Extend the base Person model for city-specific functionality.
    Add any custom fields or methods specific to your city here.
    """
    
    class Meta:
        proxy = True


class {{ cookiecutter.jurisdiction_camel_case }}Organization(Organization):
    """
    Extend the base Organization model for city-specific functionality.
    Add any custom fields or methods specific to your city here.
    """
    
    class Meta:
        proxy = True
