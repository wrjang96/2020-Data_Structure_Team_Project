from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    foodtype = models.TextField(default="한식")
    foodlist = models.TextField()
    review = models.TextField()
    score = models.IntegerField(default=0)
    LOCATION_CHOICES = (("정문 || 철문", "정문 || 철문"), ("쪽문", "쪽문"))
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default="쪽문")
    phone_number = models.CharField(max_length=15, default="02-1111-1111")

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
