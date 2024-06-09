from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateTimeField(default=datetime.now(),blank=True, null=True)

    def __str__(self):
        return f'{self.name}'