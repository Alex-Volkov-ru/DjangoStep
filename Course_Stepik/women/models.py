from django.db import models

# Create your models here.
class Women(models.Model):

    title = models.CharField(
        max_length=255
    )
    content = models.TextField(
        blank=True,
        null=True,
    )
    time_create = models.DateTimeField(
        auto_now_add=True
    )
    time_update = models.DateField(
        auto_now=True
    )
    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title
    
class Auto(models.Model):
    name = models.CharField(
        max_length=100
    )
    model = models.CharField(
        max_length=50
    )
    price = models.IntegerField(
        blank=True,
        default=0
    )
    is_exists = models.BooleanField(
        blank=True
    )