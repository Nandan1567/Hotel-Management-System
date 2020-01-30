from django.db import router
from django.urls import path,include
from .views import api_room_name_list_view, api_room_details_view, api_room_updated_view, api_room_delete_view, api__guest_list_view,Hotel_GuestList
from rest_framework import routers

appname= 'hotelapp'

urlpatterns = [
    path('', api_room_name_list_view, name='guest_list'),
    path('room/', api_room_name_list_view, name='guest'),
    path('<pk>/room', api_room_details_view, name='guest'),
    path('<pk>/update', api_room_updated_view, name='updated'),
    path('<pk>/delete', api_room_delete_view, name='delete'),
    path('guest/', api__guest_list_view, name='guest'),
    path('guest1/',Hotel_GuestList.as_view() , name='gen'),
]