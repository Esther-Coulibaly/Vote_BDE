from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'Compte'
urlpatterns = [
    path('', views.indexView, name='home_compte'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', views.registerView, name='register_url'),
    path('list_user/', views.listView, name='user_list_url'),
    path('presentation/', views.presentation, name='presentation_url'),
    path('apropos/', views.apropos, name='apropos_url'),
]
