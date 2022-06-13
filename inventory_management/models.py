import datetime

from django.db import models

# Create your models here.

building_number_choices = [
    ("BA1", "Bauabschnitt 1"),
    ("BA2", "Bauabschnitt 2")
]

floor_choices = [
    ("UG", "Untergeschoss"),
    ("EG", "Erdgeschoss"),
    ("1S", "Erster Stock"),
    ("2S", "Zweiter Stock")
]

yes_no_choice = [
    ('0', 'Gerät Funktioniert'),
    ('1', 'Gerät Funktioniert NICHT')
]


class Location(models.Model):
    class Meta:
        verbose_name = "Ort"
        verbose_name_plural = "Orte"
    building = models.CharField(max_length=10, choices=building_number_choices, default="Bauabschnitt 1", verbose_name="Bauabschnitt")
    floor = models.CharField(max_length=10, choices=floor_choices, default="1F", verbose_name="Stockwerk")

    def __str__(self):
        return f'{self.building} {self.floor}'


class Room(models.Model):
    class Meta:
        verbose_name = "Raum"
        verbose_name_plural = "Räume"

    room_name = models.CharField(max_length=10, blank=True, default=None, verbose_name="Raum Bezeichung")
    room_location = models.ForeignKey(Location, blank=False, on_delete=models.SET_NULL, null=True, verbose_name="Raum Ort")

    def __str__(self):
        return f'{self.room_name}'


# Device Handling
#####################################################################################################################


class DeviceCategory(models.Model):
    """
    Device Category
    for Smartphones, SmartBoards, Speaker, Computer, etc..
    """

    # changing verbose name
    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    # category name
    name = models.CharField(max_length=10, blank=True, default=None, verbose_name="Name der Kategorie")

    def __str__(self):
        return f'{self.name}'


class DeviceType(models.Model):
    # changing verbose name
    class Meta:
        verbose_name = "Geräte Typ"
        verbose_name_plural = "Geräte Typen"

    # Device Category (Smartphone)
    category = models.ForeignKey(DeviceCategory, on_delete=models.SET_NULL, default=None, verbose_name="Kategorie",
                                 null=True)
    brand = models.CharField(max_length=10, verbose_name="Marke")
    model = models.CharField(max_length=10, verbose_name="Geräte Modell")

    def __str__(self):
        return f'{self.brand} {self.model}'


class Device(models.Model):
    """
    Device
    :needs the device type
    """

    # changing verbose name
    class Meta:
        verbose_name = "Geräte"
        verbose_name_plural = "Geräte"

    # type of Device
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, default=None, verbose_name="Kategorie",
                                    null=True)
    serial_num = models.CharField(max_length=20, blank=False, default=None, verbose_name="Serien Nummer")
    production_date = models.DateField(default=datetime.date.today, verbose_name="Produktions Datum")
    warranty_date = models.DateField(default=datetime.date.today, verbose_name="Garantie Ablauf Datum")
    is_working = models.CharField(max_length=13, choices=yes_no_choice, default="Gerät Funktioniert", verbose_name="Funktonsfähig?")
    issues = models.CharField(max_length=50, default="keine Fehler", blank=True, verbose_name="Geräte Fehler")
    hints = models.CharField(max_length=50, default="keine Hinweise", blank=True, verbose_name="Hinweise")

    room = models.ForeignKey(Room, blank=True, on_delete=models.SET_NULL, null=True, verbose_name="Raum")

    def __str__(self):
        return f'{self.serial_num}'


# Other Equipment
###########################################################################

class OtherEquipment(models.Model):
    """
    Here goes the equipment like Canvas, Chairs, Desk, etc
    """
    class Meta:
        verbose_name = "Sonstige Ausstatung"
        verbose_name_plural = "Sonstige Ausstatungen"

    equipmentName = models.CharField(max_length=10, blank=False, default="Tafel", verbose_name="Sonstige Ausstatung")
    room = models.ForeignKey(Room, default=None, on_delete=models.SET_NULL, null=True, verbose_name="Raumname")

    def __str__(self):
        return f'{self.equipmentName}'
