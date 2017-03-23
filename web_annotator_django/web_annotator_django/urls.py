"""web_annotator_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mainapp.views.index'),
    url(r'^register_user/', 'mainapp.views.registerUser'),
    url(r'^login_user/', 'mainapp.views.loginUser'),
    url(r'^add_collection/', 'mainapp.views.addCollection'),
    url(r'^add_manuscript/', 'mainapp.views.addManuscript'),
    url(r'^add_page/', 'mainapp.views.addPage'),
    url(r'^add_annotation/', 'mainapp.views.addAnnotation'),    
    url(r'^get_annotations/', 'mainapp.views.getPageInfoAndAnnotations'),
    url(r'^get_annotation_html/', 'mainapp.views.getAnnotationHTML'),
    url(r'^add_files/', 'mainapp.views.addFiles'),    
]
