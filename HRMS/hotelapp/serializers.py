from rest_framework import serializers
from .models import *


class Hotel_guestSerializers(serializers.ModelSerializer):
    class Meta:

        model = Hotel_Guest
        fields = ('govt_id','guest_name', 'Guest_members')
class RoomSerializers(serializers.ModelSerializer):
    class Meta:

        model = Room
        fields = ('Room_type','add_room')

class ManagerSerializers(serializers.ModelSerializer):
    class Meta:

        model = Manager
        fields = ('roomnumber','room_type')

