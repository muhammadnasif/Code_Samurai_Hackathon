from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import observer.views as obsever_views

urlpatterns = [
    path('projects/', obsever_views.projects, name='projects'),
]