from django.conf.urls import url
from .views import func, LoginView, LogoutView,contact

urlpatterns = [
    
    url(r'^$', func, name="home"),
    url(r'^contact/',contact,name="contact"),
    url(r'^login/$', LoginView, name="login"),
    url(r'^logout/$', LogoutView, name="logout"),
]
