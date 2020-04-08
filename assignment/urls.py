"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from user import views as user_views
from songs import views as song_views
import templates
urlpatterns = [
    path('',user_views.index,name='index'),
    path('register/',user_views.register,name='register'),
    path('addsong/',song_views.SongView.as_view(),name='addsong'),
    path('addartist/',song_views.ArtistView.as_view(),name='addartist'),
    path('rating/',song_views.RatingView.as_view(),name='rating'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name= 'user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('topsongs/',song_views.topsongs,name='topsongs'),
    path('addsong/',song_views.addsong,name='addsong'),
    path('topartist/',song_views.topartist,name='topartist'),
    path('admin/', admin.site.urls),
]
