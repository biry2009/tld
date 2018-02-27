"""mydomain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from tld import views as tld_views

urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'tlds/$', tld_views.tlds, name="tlds"),
    url(r'^tlds/(?P<name>\w+)/$', tld_views.domain, name="domain"),
    url(r'^$', tld_views.index, name="index"),
    url(r'^reviews/$', tld_views.reviews, name="reviews"),
    url(r'^review/(?P<name>\w+)$', tld_views.review, name="review"),
    url(r'^about/$', tld_views.about, name="about"),
    url(r'^contact/$', tld_views.contact, name="contact"),
    url(r'^mylogin/', admin.site.urls),
    url(r'^blog/$', tld_views.blogindex, name='blog'),
    url(r'^blog/(?P<slug>[-\w]+)/$', tld_views.detail, name='detail'),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)