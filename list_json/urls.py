from django.urls import path
from . import views

urlpatterns = [
    path('json/',views.list_json,name='json'),
    path('json_raw/',views.json_raw,name='json_raw')
]