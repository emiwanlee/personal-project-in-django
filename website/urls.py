"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage ),
    path('premiership.html', views.premiership),
    path('belgian_pro_league.html', views.Belgian1),
    path('championship.html', views.Championship),
    path('league_one.html', views.League1),
    path('english_league_two.html', views.League2),
    path('german_bundesliga.html', views.GermanBundesliga),
    path('german_bundesliga_2.html', views.GermanBundesliga2),
    path('greek_super_league.html', views.GreekSuperLeague),
]
