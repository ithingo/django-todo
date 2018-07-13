from django.urls import path

from . import views

urlpatterns = [
    path('', views.MyBaseTemplateView.as_view(), name='add_item'),
    path('', views.MyBaseTemplateView.as_view(), name='actions_panel'),
]
