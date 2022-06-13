from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Room
from .models import Device
from .models import DeviceCategory
from .forms import FilterFormRooms
from .forms import FilterFormDevices
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import OtherEquipment
from django.contrib.auth.models import User


# from .forms import FilterForm


# Create your views here.

def home(request):
    return render(request, 'inventory_management/home.html')


class RoomListView(ListView):
    model = Room
    paginate_by = 10

    def get_queryset(self):
        query_search = self.request.GET.get('search')
        form = FilterFormRooms(self.request.GET or None)
        if form.is_valid():
            query_search_advanced = form.cleaned_data
            room = query_search_advanced['room']
            floor = query_search_advanced['floor']
            building = query_search_advanced['building']
            print(len(room))
            if len(room) == 0:
                return Room.objects.filter(
                    Q(room_location__floor=floor) & Q(room_location__building=building)
                )
            else:
                return Room.objects.filter(
                    Q(room_name=room) & Q(room_location__floor=floor) & Q(room_location__building=building)
                )
        if query_search is not None:
            return Room.objects.filter(
                Q(room_name__contains=query_search) | Q(room_location__building__contains=query_search) |
                Q(room_location__floor__contains=query_search))
        return Room.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        f1 = FilterFormRooms()
        context['form'] = f1
        return context


class DeviceListView(ListView):
    model = Device
    paginate_by = 10


    def get_queryset(self):
        query_search = self.request.GET.get('search_dev')
        if query_search == "":
            return Device.objects.all()
        form = FilterFormDevices(self.request.GET or None)
        if form.is_valid():
            query_search_advanced = form.cleaned_data
            print(query_search_advanced)
            category = query_search_advanced['device_category']
            type = query_search_advanced['device_types']
            work = query_search_advanced['device_works']
            production = query_search_advanced['production']
            split_model = str(type).split(" ")
            work_converter = {
                '0': True,
                '1': False
            }
            return Device.objects.filter(
                Q(device_type__category__name__contains=category) &
                Q(device_type__brand__contains=split_model[0]) &
                Q(device_type__model__contains=split_model[1])
            ).order_by(production)

        if query_search is not None:
            return Device.objects.filter(
                Q(device_type__category__name__contains=query_search) |
                Q(device_type__brand__contains=query_search) |
                Q(device_type__model=query_search) |
                Q(device_type__device__serial_num__contains=query_search))

        return Device.objects.all()

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super(DeviceListView, self).get_context_data(**kwargs)
            f1 = FilterFormDevices
            context['form'] = f1
            return context
        else:
            self.template_name = 'inventory_management/no_login.html'
            redirect('device_list')
            return {}


class DeviceDetailView(DetailView):
    model = Device

    def get_context_data(self, **kwargs):
        context = super(DeviceDetailView, self).get_context_data(**kwargs)
        return context


class RoomDetailView(DetailView):
    model = Room


class OtherEquipmentListView(ListView):
    model = OtherEquipment


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign_up.html"


class UserDetailView(DetailView):
    model = User


