from django.urls import path
from . import views

from iwear.views import homepage

app_name = 'iwear'
urlpatterns = [
    #path('accounts/login/', views.login, name='login'),
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('setting/', views.setting, name='setting'),
    # path('addShow/', views.post_create, name='addShow'),
    path('addEdit/', views.post_create, name='addEdit'),
    path('record/', views.record, name='record'),
    path('search/', views.search, name='search'),
    path('Accessories/', views.access, name='Accessories'),
]