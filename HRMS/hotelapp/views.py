from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


#
# class HotelGuestView(viewsets.ModelViewSet):
#     serializer_class = Hotel_guestSerializers
#     queryset = Hotel_Guest.objects.all()
#
#
# class RoomView(viewsets.ModelViewSet):
#     serializer_class = RoomSerializers
#     queryset = Room.objects.all()
#
#
# class ManagerView(viewsets.ModelViewSet):
#     serializer_class = ManagerSerializers
#     queryset = Manager.objects.all()


@api_view(['GET', ])
def api_room_name_list_view(request):
    guest = Room.objects.all()
    if request.method == 'GET':
        serializer = RoomSerializers(guest, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def api_room_details_view(request, pk):
    if request.method == 'GET':
        try:
            guest = Room.objects.get(add_room=pk)
        except Room.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = RoomSerializers(guest)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_room_updated_view(request, pk):
    if request.method == 'PUT':
        try:
            guest = Room.objects.get(add_room=pk)
        except Room.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        else:
            serializer = RoomSerializers(guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_200_OK)
            return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_room_delete_view(request, pk):
    try:
        guest = Room.objects.get(add_room=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation = guest.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
            return Response(data, status.HTTP_200_OK)


@api_view(['POST', ])
def api_room_PO_view(request, pk):
    if request.method == 'POST':
        try:
            guest = Room.objects.get(add_room=pk)
        except Room.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        else:
            serializer = RoomSerializers(guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_200_OK)
            return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def api__guest_list_view(request):
    guest = Hotel_Guest.objects.all()
    if request.method == 'GET':
        serializer = Hotel_guestSerializers(guest, many=True)
    return Response(serializer.data)


class Hotel_GuestList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

    # def get_queryset(self):
    #     guest = self.request.
    #     return guest.objects.all()
