from django.db import models

# Create your models here.


class Product(models.Model):
    SECTIONS = (
        ('Home', 'Home'),
        ('Ofice', 'Office'),
    )
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    section = models.CharField(max_length=20, choices=SECTIONS)
    picture = models.ImageField(
        height_field=None, width_field=None, max_length=100, upload_to='product/uploads')
    # amont =
    # price =
    # code =

    def __str__(self):
        return self.tittle
