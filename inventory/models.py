from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)


class Comments(models.Model):
    product = models.ForeignKey(Product, related_name='comments')
    title = models.CharField(max_length=255)
    comments = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User)