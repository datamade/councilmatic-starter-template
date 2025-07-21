import os
from django.shortcuts import render
from django.views.generic import TemplateView

from councilmatic_core.models import Bill, Event, Person


class IndexView(TemplateView):
    template_name = "home_page.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "bill_count": Bill.objects.count(),
            "event_count": Event.objects.count(),
            "person_count": Person.objects.count(),
        })
        return context


def robots_txt(request):
    """Serve robots.txt file with crawling permissions based on environment."""
    return render(
        request,
        "robots.txt",
        {"ALLOW_CRAWL": os.getenv("ALLOW_CRAWL", "False").lower() == "true"},
        content_type="text/plain",
    )


def page_not_found(request, exception, template_name="404.html"):
    """Custom 404 error handler."""
    return render(request, template_name, status=404)


def server_error(request, template_name="500.html"):
    """Custom 500 error handler."""
    return render(request, template_name, status=500)
