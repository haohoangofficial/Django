from django.urls import path

from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.loginPage, name='loginPage'),
    path('signup/', views.signupPage, name='signupPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
]