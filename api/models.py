from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    description = models.TextField()
    photo = models.ImageField(upload_to='products')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.id} - {self.user.username}'
