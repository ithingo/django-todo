from django.urls import path

from . import views

urlpatterns = [
    path('', views.TemplateView.add_task, name='add_task'),
]
