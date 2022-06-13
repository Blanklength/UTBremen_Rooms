from django import forms
from .models import DeviceCategory
from .models import Room
from .models import floor_choices
from .models import building_number_choices
from .models import Location
from .models import DeviceCategory
from .models import DeviceType
from .models import yes_no_choice


def convert_to_choices(Name):
    choices = []
    i = 0
    for oneName in Name.objects.all():
        current_object = (oneName, oneName)
        choices.append(current_object)
        i += 1
    return choices


warranty_choice = [
    ('Garantie laufend', 'Garantie laufend'),
    ('Garantie laufend', 'Garantie abgelaufen')
]


production_date_choice = [
    ('production_date', 'Order By Production Date'),
    ('name', 'Order By Alphabet'),
]

room_choices = convert_to_choices(Room)
location_choices = convert_to_choices(Location)
device_cat_choices = convert_to_choices(DeviceCategory)
device_type_choices = convert_to_choices(DeviceType)


class FilterFormRooms(forms.Form):
    room = forms.ChoiceField(choices=room_choices, required=False, label="Räume")
    floor = forms.ChoiceField(choices=floor_choices, label="Stockwerke")
    building = forms.ChoiceField(choices=building_number_choices, label="Bauabschnitt")


class FilterFormDevices(forms.Form):
    device_category = forms.ChoiceField(choices=device_cat_choices, required=False, label="")
    device_types = forms.ChoiceField(choices=device_type_choices, required=False, label="")
    device_works = forms.ChoiceField(choices=yes_no_choice, required=False, label="")
    production = forms.ChoiceField(choices=production_date_choice, required=False, label="")
