"""board URL Configuration

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
from django.contrib import admin
from list_posts import views
from write_article import views as views2
from login import views as views3

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # if login
    url(r'^login/', include('login.urls')),
    # by default, list posts.
    # url(r'^$',views.give_post_tag ),
    url(r'^$', include('list_posts.urls')),
    # url routing to list_posts
    url(r'^posts/', include('list_posts.urls')),
    # if posting a comment
    url(r'^posting/', views.handle_comment),
    # url routing to write
    url(r'^write/', include('write_article.urls')),
    # if posting an article
    url(r'^posting2/', views2.handle_article),
    # twitter login
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
