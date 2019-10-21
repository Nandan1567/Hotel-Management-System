from django.test import TestCase
from .models import Room,Manager,Hotel_Guest,Booking_records

class RoomTestCase(TestCase):
   def setUp(self):
       Room.objects.create(Room_type = 'AC',)

   def test_guest_name(self):
       room = Room.objects.get(Room_type = 'AC')
       self.assertEqual(room.Room_type,'AC')



class Hotel_GuestTestcase(TestCase):
    def setUp(self):
        hotel=Hotel_Guest.object.create(Room_type='ac',add_room=101)
        Hotel_Guest.objects.create(guest_name='nandan',Guest_members=3,guest_phone_number=9449049179,guest_address='chikmagalur',roomType=hotel)
    def hotel_guest(self):
        guest=Hotel_Guest.objects.get(guest_name='nandan')
        self.assertEqual(guest.guest_name,'nandan')

class ManagerTestcase(TestCase):
    def setUp(self):
        manager=Manager.objects.create(Room_type='ac')
        manager_guset=Manager.objects.create(guest_name='nandan',Guest_members=3,guest_phone_number=9449049179,guest_address='chikmagalur')
        Manager.create.objects.create(room_type=manager)
        Manager.objects.create(guset=manager_guset)
    def manager_Test(self):
        manager1=Manager.objects.get(guest_name='nandan')
        self.assertEqual(manager1.guest_name,'nandan')
