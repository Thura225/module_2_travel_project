from django.urls import path
from .views import buseslist,busescreate,busesdelete,busesupdate


urlpatterns = [
    path('', buseslist,name="buseslist"),
    path('create',busescreate,name="buscreate"),
    path('<int:bus_id>/update',busesupdate,name="busupdate"),
    path('<int:bus_id>/delete',busesdelete,name="busdelete")
]