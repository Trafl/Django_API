from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openia_api.client import get_car_bio


def cars_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ia_bio = get_car_bio(instance.model, instance.brand, instance.year)
        instance.bio = ia_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_inventory_update()
