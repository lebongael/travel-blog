"""travelblog URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    # Admin pages
    url(r'^management/', admin.site.urls),
    # Static Pages
    url(r'^$', TemplateView.as_view(
        template_name='travelblog/index.html'), name='index'),
    url(r'^crew/', TemplateView.as_view(
        template_name='travelblog/crew.html'), name='crew'),
    # Photo gallery
    url(r'^galleries/', include('galleries.urls'), name='galleries'),
    # Blog
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
