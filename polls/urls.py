from django.urls import path

from . import views

# These are the handlers for forms(!!!) instead of urls, do not remove
urlpatterns = [
    path('', views.MyBaseTemplateView.as_view(), name='add_item'),
    path('', views.MyBaseTemplateView.as_view(), name='delete_item'),
    path('', views.MyBaseTemplateView.as_view(), name='change_item'),
    path('', views.MyBaseTemplateView.as_view(), name='actions_panel'),
    path('', views.MyBaseTemplateView.as_view(), name='tabs'),
    path('', views.MyBaseTemplateView.as_view(), name='counters'),

    # on double click updating, try
    path('', views.MyBaseTemplateView.as_view(), name='update_item')
]
