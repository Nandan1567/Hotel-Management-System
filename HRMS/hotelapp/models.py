from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Room(models.Model):
    Room_type = models.CharField(max_length=200)
    add_room = models.IntegerField(primary_key=True)
    room_number = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return str(self.Room_type)+','+str(self.add_room)


class Hotel_Guest(models.Model):
    govt_id = models.IntegerField(primary_key=True)
    roomType = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    Guest_members = models.IntegerField(default=0)
    guest_phone_number = models.IntegerField(default=0)
    guest_address = models.CharField(max_length=200)
    bookingdate = models.DateField()
    returndate = models.DateField()

    def __str__(self):
        return self.guest_name


class Manager(models.Model):
    roomnumber = models.IntegerField(primary_key=True)
    room_type = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    guset = models.ForeignKey(Hotel_Guest, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_type)


class Booking_records(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    Booking_date = models.DateField()
    Booking_room = models.ForeignKey(Manager, null=True, on_delete=models.CASCADE)
    Guest_details = models.ForeignKey(Hotel_Guest, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    room_rate = models.FloatField()
    cancel_booking = models.BooleanField()
    return_date = models.DateField()
    checkout_room = models.BooleanField()

    def cal(self):
        total = (self.return_date - self.Booking_date).days
        total_cost_of_guest = total * self.room_rate
        return total_cost_of_guest

    cal.short_description = 'Total Cost'


@receiver(post_save, sender=Booking_records)
def records(sender, instance, **kwargs):
    stock = instance.room.available
    if stock > 0:
        stock -= 1
        room1 = instance.room
        instance.room.available = stock
        room1.save()
        return True
