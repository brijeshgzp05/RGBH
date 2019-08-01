from django.conf.urls import  url
from .views import StudentRegisterView, StudentListView ,StudentDetailView, StudentUpdateView, StudentDeleteView, StudentPendingView,StudentSearchView

urlpatterns = [
   
    url(r'^add/', StudentRegisterView, name="add"),
    url(r'^list/', StudentListView, name="list"),
    url(r'^$', StudentSearchView, name="search"),
    url(r'^pending-list/', StudentPendingView, name="pending_list"),
    url(r'^(?P<slug>[\w-]+)/$', StudentDetailView, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', StudentUpdateView, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', StudentDeleteView, name='delete'),
]
