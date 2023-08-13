from django.urls import path
from .views import user_login
from . import views

urlpatterns = [
    # 他のURLパターン...
    path('login/', user_login, name='user_login'),
]
