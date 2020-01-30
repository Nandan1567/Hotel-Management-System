from django import forms
from django.contrib import admin

from .models import Room, Manager, Booking_records, Hotel_Guest


class RoomAdmin(admin.ModelAdmin):
    list_display = ('Room_type',)
    ordering = ['Room_type']


admin.site.register(Room, RoomAdmin)


class GusetAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GusetAdminForm, self).__init__(*args, **kwargs)

    def clean(self):

        room_number1 = self.cleaned_data.get('Guest_members')
        checkin = self.cleaned_data.get('bookingdate')
        checkout = self.cleaned_data.get('returndate')

        if room_number1 > 5:
            raise forms.ValidationError(f'enter 3 members', code='invalid')
        if checkin == checkout:
            raise forms.ValidationError(f'same date not booking', code='invalid')

        return self.cleaned_data

    def save(self, commit=True):
        return super(GusetAdminForm, self).save(commit=commit)


class GustAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'Guest_members', 'guest_phone_number', 'guest_address')
    form = GusetAdminForm


admin.site.register(Hotel_Guest, GustAdmin)


class ManagerAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ManagerAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        member = self.cleaned_data.get('guset')
        member1 = self.cleaned_data.get('roomnumber')
        if member.roomType.add_room != member1:
            raise forms.ValidationError(f'room is not available', code='invalide')
        return self.cleaned_data

    def save(self, commit=True):
        return super(ManagerAdminForm, self).save(commit=commit)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('room_type',)
    form = ManagerAdminForm


admin.site.register(Manager, ManagerAdmin)


class Booking_recordsAdmin(admin.ModelAdmin):
    list_display = (
        'Booking_ID', 'Booking_date', 'Booking_room', 'return_date', 'room_rate', 'cal', 'checkout_room',
        'cancel_booking')
    ordering = ['Booking_ID']


admin.site.register(Booking_records, Booking_recordsAdmin)

# Register your models here.
