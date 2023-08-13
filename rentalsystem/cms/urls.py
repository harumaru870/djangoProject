from django.urls import path
from .views import user_login,dashboard
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # 他のURLパターン...
    path('login/', user_login, name='user_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
