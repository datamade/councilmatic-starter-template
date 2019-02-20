"""councilmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView
from haystack.query import EmptySearchQuerySet
from councilmatic_core.views import CouncilmaticSearchForm, CouncilmaticFacetedSearchView
from pittsburgh.views import PittsburghCouncilmaticFacetedSearchView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', PittsburghCouncilmaticFacetedSearchView(searchqueryset=EmptySearchQuerySet,
                                       form_class=CouncilmaticSearchForm), name='search'),
    # url(r'^search/', CouncilmaticFacetedSearchView(searchqueryset=sqs, 
    #                                    form_class=CouncilmaticSearchForm)),
    url(r'', include('councilmatic_core.urls')),
]

urlpatterns += staticfiles_urlpatterns()
