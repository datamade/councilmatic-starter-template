from councilmatic_core.haystack_indexes import BillIndex
from haystack import indexes
from .models import CityBill
from datetime import datetime
from django.conf import settings
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)

class CityBillIndex(BillIndex, indexes.Indexable):

    def get_model(self):
        return CityBill

