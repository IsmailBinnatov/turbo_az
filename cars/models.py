from django.db import models


class SaleStatus(models.Model):
    status = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'{self.status}'

    class Meta:
        verbose_name = 'Sale status'
        verbose_name_plural = 'Sales status'


class CarСondition(models.Model):
    status = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'{self.status}'

    class Meta:
        verbose_name = 'Car condition'
        verbose_name_plural = 'Cars conditions'

class MarketVersion(models.Model):
    version = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'{self.version}'

    class Meta:
        verbose_name = 'Market version'
        verbose_name_plural = 'Market version'


class PlaceCount(models.Model):
    count = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f'{self.count}'

    class Meta:
        verbose_name = 'Place count'
        verbose_name_plural = 'Places count'


class OwnerCount(models.Model):
    count = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.count}'

    class Meta:
        verbose_name = 'Owner count'
        verbose_name_plural = 'Owners count'


class MeasureUnit(models.Model):
    measure_unit = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.measure_unit}'

    class Meta:
        verbose_name = 'Measure unit'
        verbose_name_plural = 'Measure unit'


class EngineVolume(models.Model):
    engine = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.engine}'

    class Meta:
        verbose_name = 'Engine volume'
        verbose_name_plural = 'Engine volume'


class Transmission(models.Model):
    transmission = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.transmission}'


class DriveWheel(models.Model):
    drive_wheel = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.drive_wheel}'


class FuelType(models.Model):
    fuel_type = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.fuel_type}'


class Color(models.Model):
    color = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.color}'


class BanType(models.Model):
    ban = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.ban}'


class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class CarBrand(models.Model):
    car_brand = models.CharField(max_length=64)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.car_brand}'


class CarModel(models.Model):
    car_brand = models.ForeignKey(
        'CarBrand', on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.model}'


class MoneyCurrency(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class CarPhoto(models.Model):
    car_photo = models.ImageField(
        upload_to='uploads/cars/', null=True, blank=True)


class Car(models.Model):
    car_brand = models.ForeignKey(
        'CarBrand', on_delete=models.SET_NULL, null=True, blank=True)
    car_model = models.ForeignKey(
        'CarModel', on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.ForeignKey(
        'MoneyCurrency', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(
        'City', on_delete=models.SET_NULL, null=True, blank=True)
    ban = models.ForeignKey(
        'BanType', on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(
        'Color', on_delete=models.SET_NULL, null=True, blank=True)
    fuel = models.ForeignKey(
        'FuelType', on_delete=models.SET_NULL, null=True, blank=True)
    drive_wheel = models.ForeignKey(
        'DriveWheel', on_delete=models.SET_NULL, null=True, blank=True)
    transmission = models.ForeignKey(
        'Transmission', on_delete=models.SET_NULL, null=True, blank=True)
    engine_volume = models.ForeignKey(
        'EngineVolume', on_delete=models.SET_NULL, null=True, blank=True)
    measure_unit = models.ForeignKey(
        'MeasureUnit', on_delete=models.SET_NULL, null=True, blank=True)
    owners_count = models.ForeignKey(
        'OwnerCount', on_delete=models.SET_NULL, null=True, blank=True)
    place_count = models.ForeignKey(
        'PlaceCount', on_delete=models.SET_NULL, null=True, blank=True)
    mileage = models.PositiveSmallIntegerField(null=True, blank=True)
    horse_power = models.PositiveSmallIntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)
    has_alloy_wheels = models.BooleanField(default=False)
    has_abs = models.BooleanField(default=False)
    has_hatch = models.BooleanField(default=False)
    has_rain_sensor = models.BooleanField(default=False)
    has_central_locking_system = models.BooleanField(default=False)
    has_parktronic = models.BooleanField(default=False)
    has_air_conditioner = models.BooleanField(default=False)
    has_seat_heating = models.BooleanField(default=False)
    has_seat_ventilation = models.BooleanField(default=False)
    has_leather_interior = models.BooleanField(default=False)
    has_xenon = models.BooleanField(default=False)
    has_rear_view_camera = models.BooleanField(default=False)
    has_side_curtains = models.BooleanField(default=False)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    car_photo = models.ForeignKey(
        'CarPhoto', on_delete=models.SET_NULL, null=True, blank=True)
