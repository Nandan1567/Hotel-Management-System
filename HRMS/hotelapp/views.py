from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class HotelGuestView(viewsets.ModelViewSet):
    serializer_class = Hotel_guestSerializers
    queryset = Hotel_Guest.objects.all()


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()

