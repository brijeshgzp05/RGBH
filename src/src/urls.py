"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import func
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', func, name="home"),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^menu/', include('menu.urls', namespace="menu")),
    url(r'^staff/', include('staff.urls', namespace="staff")),
    url(r'^rooms/', include('room.urls', namespace="room")),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)