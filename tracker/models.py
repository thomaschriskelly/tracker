from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description

class Breadcrumb(models.Model):
    product = models.ForeignKey(Product)
    datetime = models.DateTimeField()
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)
    elevation = models.CharField(max_length=32)

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(
            self.product,
            self.datetime,
            self.longitude,
            self.latitude,
            self.elevation,
        )
