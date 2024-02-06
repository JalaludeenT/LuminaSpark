from django.urls import path
from . import views

app_name = 'BANK'

urlpatterns = [
    path('', views.logo, name='home'),
    path('home', views.home, name='home'),
    path('locations/', views.locations, name='locations'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('create_account/', views.create_account_view, name='create_account'),
    path('account_login/', views.account_login, name='account_login'),
    path('account/profile/<int:account_id>/', views.profile, name='profile'),
    path('profile/<int:account_id>/details', views.account_details_view, name='details'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('logout/', views.logout, name='logout'),
]
