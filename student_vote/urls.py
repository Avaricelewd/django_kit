from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('index2/',views.index,name='index2'),
    path("select/",views.select,name="select"),
    path("add/",views.add,name='add'),
    path('result/',views.result,name='result'),

]