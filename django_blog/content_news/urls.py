""" Router configuration for ContentNews.
"""
# pylint:disable=invalid-name

from django.conf.urls import url

from .views import list_view

urlpatterns = [
    url('^$', list_view, name='index'),
]
