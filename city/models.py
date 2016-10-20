from django.conf import settings
from django.db import models
from councilmatic_core.models import Bill, Event
from datetime import datetime
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)

class CityBill(Bill):
     
    class Meta:
        proxy = True
