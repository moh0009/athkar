from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile,name="profile"),
    path('logout/', views.logout, name="logout"),
    path('', views.main, name="main"),
    path('athkar/<int:num>', views.athkar, name="athkar"),
    path('add/', views.thkr, name="add"),
    path('athkar/', views.main, name="main"),
]
