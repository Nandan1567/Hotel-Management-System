from rest_framework import serializers

import hotelapp
from .models import *

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('Room_type', 'add_room','room_number','available')


class Hotel_guestSerializers(serializers.ModelSerializer):
    roomType = RoomSerializers()

    class Meta:
        model = Hotel_Guest
        fields = ('govt_id', 'guest_name', 'Guest_members', 'roomType','guest_phone_number','guest_address','bookingdate','returndate')


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('roomnumber', 'room_type')
