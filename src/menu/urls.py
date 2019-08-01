from django.conf.urls import url
from .views import MenuListView, MenuUpdateView

urlpatterns = [
    
    url(r'^$', MenuListView, name="menu"),
    url(r'^(?P<id>\d+)/$', MenuUpdateView, name='update'),
    
]