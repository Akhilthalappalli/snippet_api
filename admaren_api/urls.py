from django.contrib import admin
from django.urls import path , include
from admaren_api import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
]
