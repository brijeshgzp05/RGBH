from django.conf.urls import url

from .views import RoomAddView, RoomListView, RoomDetailView

urlpatterns = [

    url(r'^add/$',RoomAddView,  name="add"),
    url(r'^$',RoomListView,  name="list"),
    url(r'^(?P<id>\d+)/$', RoomDetailView, name='detail'),
    
]