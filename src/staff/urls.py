from django.conf.urls import url
from .views import StaffListView

urlpatterns = [
    url(r'^$',StaffListView , name="staff"),
]

