from django.urls import path

from . import views

urlpatterns = [
    path('', views.TemplateView.as_view()),
    # path('ajax/add_item', views.add_item, name='add_item')
]
