
from django.urls import path
from . import views

urlpatterns = [

    # fill in here with urls

    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('account/', views.accountPage, name='account'),
    path('order/', views.orderPage, name='order'),

    path('admin/', views.adminPage, name='admin'),
    path('order_confirmation/', views.orderConfirmation, name='order_confirmation'),
    path('create_account/', views.createAccountPage, name='create_account'),
    path('drones/', views.dronesPage, name='drones'),

    path('drone_registration', views.droneRegistrationPage, name='drone_registration'),
]