from django.urls import path
from . import views

urlpatterns = [
    path('haxi_list/',views.haxi_list,name='haxi_list'),
]