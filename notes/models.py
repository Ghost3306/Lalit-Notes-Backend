from django.db import models
from django.utils import timezone
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField()
    user = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=True)