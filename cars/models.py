from django.db import models


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
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    car_photo = models.ForeignKey(
        'CarPhoto', on_delete=models.SET_NULL, null=True, blank=True)


class CarPhoto(models.Model):
    car_photo = models.ImageField(
        upload_to='uploads/cars/', null=True, blank=True)
