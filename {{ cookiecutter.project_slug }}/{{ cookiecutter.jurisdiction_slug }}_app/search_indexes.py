from councilmatic_search.search_indexes import BillIndex
from haystack import indexes
from .models import {{ cookiecutter.jurisdiction_camel_case }}Bill
from django.conf import settings
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)

class {{ cookiecutter.jurisdiction_camel_case }}BillIndex(BillIndex, indexes.Indexable):

    def get_model(self):
        return {{ cookiecutter.jurisdiction_camel_case }}Bill

