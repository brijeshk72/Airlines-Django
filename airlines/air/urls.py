from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('<int:dl>/', views.delete, name='delete'),
    path('show', views.show, name='show'),
    path('<int:buy_id>', views.buy, name='buy'),
    path('confirm', views.confirm, name='confirm'),
    path('/<str:e_pk>/', views.ticket, name='ticket'),
]