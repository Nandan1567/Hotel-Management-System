from django.test import TestCase
from .models import Room,Manager,Hotel_Guest,Booking_records

class RoomTestCase(TestCase):
   def setUp(self):
       Room.objects.create(Room_type = 'AC',)

   def test_guest_name(self):
       room = Room.objects.get(Room_type = 'AC')
       self.assertEqual(room.Room_type,'AC')



class Hotel_GuestTestcase(TestCase):
    hotel=Hotel_Guest.objects.create()