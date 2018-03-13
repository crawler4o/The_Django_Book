"""My_first_django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

from My_first_django_site.views import hello
from My_first_django_site.views import time_one
from My_first_django_site.views import time_one_plus
from My_first_django_site.views import time_two
from My_first_django_site.views import time_three
from My_first_django_site.views import time_two_plus
from My_first_django_site.views import request_meta

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^hello/$', hello),
    re_path(r'^time/one$', time_one),
    re_path(r'^time/one/plus/(\d{1,2})/$', time_one_plus),
    re_path(r'^time/two$', time_two),
    re_path(r'^time/three$', time_three),
    re_path(r'^time/two/plus/(\d{1,2})/$', time_two_plus),
    re_path(r'^meta/$', request_meta),
    re_path(r'^', include('books.urls')),
]
