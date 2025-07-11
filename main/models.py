from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True)
    hours = models.CharField(max_length=100)
    has_kitchen = models.BooleanField(default=False)
    has_bakery = models.BooleanField(default=False)
    has_delivery = models.BooleanField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} — {self.city}"


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Продукты'),
        ('drinks', 'Напитки'),
        ('home', 'Товары для дома'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_discounted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
