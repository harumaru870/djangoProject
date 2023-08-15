from django.urls import path
from .views import user_login,dashboard
from django.contrib.auth.views import LogoutView
from . import views
from .views import borrow_items, return_items


urlpatterns = [
    # 他のURLパターン...
    path('login/', user_login, name='user_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
        path('borrow/', borrow_items, name='borrow_items'),
        path('return/', return_items, name='return_items'),
        path('borrow/<int:item_id>/', views.borrow_item, name='borrow_item'),
    path('return/<int:action_id>/', views.return_item, name='return_item'),
]
