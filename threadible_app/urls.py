from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^workspaces/create$', views.create_workspace, name="index"),
    url(r'^cells/edit$', views.edit_cell, name="index"),
]