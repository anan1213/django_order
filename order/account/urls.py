from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

]
