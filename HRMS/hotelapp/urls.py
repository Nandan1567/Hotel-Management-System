from django.db import router
from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('hotel', views.HotelGuestView)
router.register('room', views.RoomView)
router.register('manager', views.ManagerView)


urlpatterns = [
    path('', include(router.urls))
]