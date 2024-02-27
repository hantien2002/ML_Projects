from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Calendar(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField(default=30)
    last_modified = models.DateTimeField(auto_now=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
