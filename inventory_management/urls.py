from django.urls import path, register_converter

from . import views
from .views import RoomListView
from .views import DeviceListView
from .views import RoomDetailView
from .views import DeviceDetailView
from .views import SignUpView
from .views import OtherEquipmentListView
from .views import UserDetailView


urlpatterns = [
    path('', views.home, name="home"),
    path('roomview', RoomListView.as_view(), name="room_list"),
    path('deviceview', DeviceListView.as_view(), name="device_list"),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name="device_detail"),
    path('room/<int:pk>/', RoomDetailView.as_view(), name="device_detail"),
    path('signup/', SignUpView.as_view(), name="sign_up"),
    path('OtherEquipment/', OtherEquipmentListView.as_view(), name="otherequipment"),
]