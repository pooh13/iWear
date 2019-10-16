"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

from iwear.views import homepage

app_name = 'iwear'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.homepage, name='homepage'),
    # path('index/', views.)
    path('profile/', views.profile, name='profile'),
    path('profile_test/<pk>', views.profile_test, name='profile_test'),
    path('follow/', views.follow, name='follow'),
    path('friend/', views.friend, name='friend'),
    path('addPost/', views.post_create, name='add_post'),
    path('record/', views.record, name='record'),
    path('search/', views.search, name='search'),
]