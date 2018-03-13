

from django.urls import path
from django.urls import re_path
from books import views


urlpatterns = [
    # re_path(r'^search-form/$', views.search_form), # no longer needed
    re_path(r'^search/$', views.search)
]
