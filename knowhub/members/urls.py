from django.urls import path
from .views import UserRegisterView,UserLogoutView
from django.contrib.auth import logout

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('logout/',UserLogoutView.as_view(),name='logout')
]