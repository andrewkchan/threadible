from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^eval/$', views.eval, name="eval"),
    #url(r'^$',TemplateView.as_view(template_name = 'input_form.html')),
    #url(r'^result/', 'login', name = 'login'))
]