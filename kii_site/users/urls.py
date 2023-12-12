from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('feedback/', views.feedback, name = 'feedback'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
