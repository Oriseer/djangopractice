from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('registration/', views.register, name='registration'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('update_customer/<str:pk>/', views.update_customer, name='update_customer'),
    path('user_page', views.user_page, name='user_page'),
]