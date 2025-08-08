from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("admin/", admin.site.urls),
    path("", include("councilmatic_search.urls")),
    path("", include("councilmatic_cms.urls")),
]

# Error handlers
handler404 = "{{ cookiecutter.jurisdiction_slug }}_app.views.page_not_found"
handler500 = "{{ cookiecutter.jurisdiction_slug }}_app.views.server_error"

# Debug toolbar and static files for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
