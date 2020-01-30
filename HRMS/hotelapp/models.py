from django.db import models


class Room(models.Model):
    Room_type = models.CharField(max_length=200)
    add_room = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.Room_type)


class Hotel_Guest(models.Model):
    govt_id = models.IntegerField(primary_key=True)
    roomType = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    Guest_members = models.IntegerField()
    guest_phone_number = models.IntegerField()
    guest_address = models.CharField(max_length=200)
    bookingdate=models.DateField()
    returndate=models.DateField()

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
    room_rate = models.FloatField()
    checkout_room = models.BooleanField()
    cancel_booking = models.BooleanField()
    return_date = models.DateField()

    def cal(self):
        total = (self.return_date - self.Booking_date).days
        total_cost_of_guest = total * self.room_rate
        return total_cost_of_guest

    cal.short_description = 'Total Cost'
