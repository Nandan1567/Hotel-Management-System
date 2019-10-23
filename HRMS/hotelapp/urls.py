from django.db import router
from django.urls import path,include
from .views import api_room_name_list_view, api_room_details_view, api_room_updated_view, api_room_delete_view
from rest_framework import routers

appname= 'hotelapp'

urlpatterns = [
    path('', api_room_name_list_view, name='guest_list'),
    path('room/', api_room_name_list_view, name='guest'),
    path('room/<pk>/', api_room_details_view, name='guest'),
    path('update/<pk>/', api_room_updated_view, name='updated'),
    path('delete/<pk>/', api_room_delete_view, name='delete'),
]