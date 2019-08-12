from django.urls import path
from  . import views

urlpatterns = [
    path('b64/',views.b64,name='b64'),
    path('b64_j/',views.b64_j,name='b64_j')
]