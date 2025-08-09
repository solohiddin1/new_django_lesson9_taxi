from django.urls import path
from .views import home,manage_users,AddTarifView,ClientListView , DriverListView, AddClientView, AddDriverView, AddDealView,UpdateClient,UpdateDriver,DeleteClient,DeleteDriver


urlpatterns = [

    path('',home,name='home'),
    path('client_dashboard/',ClientListView.as_view(),name='client'),
    path('driver_dashboard/',DriverListView.as_view(),name='driver'),
    path('add_tarif/',AddTarifView.as_view(),name='add_tarif'),
    path('add_client/',AddClientView.as_view(),name='add_client'),
    path('add_driver/',AddDriverView.as_view(),name='add_driver'),
    path('add_deal/',AddDealView.as_view(),name='add_deal'),
    path('admin_panel/',manage_users,name='admin_panel'),

    path('update_driver/<int:pk>',UpdateDriver.as_view(),name='update_driver'),
    path('delete_driver/<int:pk>',DeleteDriver.as_view(),name='delete_driver'),
    path('update_client/<int:pk>',UpdateClient.as_view(),name='update_client'),
    path('delete_client/<int:pk>',DeleteClient.as_view(),name='delete_client'),

]