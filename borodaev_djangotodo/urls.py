"""borodaev_djangotodo URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]
