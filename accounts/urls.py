from django.urls import path
from django.contrib.auth import views as auth_views # django default for login and logout
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # render the template_name
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'), # will go to next_page after after execution
    path('register/', views.RegisterView.as_view(), name='register'),
]
