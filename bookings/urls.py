from django.urls import path
from .views import bookinglists,bookingcreate,bookingdelete


urlpatterns = [
    path('', bookinglists,name="bookinglists"),
    path('<int:book_id>/delete', bookingdelete,name="bookingdelete"),
    path('buses/<int:bus_id>/create', bookingcreate,name="bookingcreate"),
]