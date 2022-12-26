from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models below here
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateField(default=timezone.now, null=True, blank=True)
    desc = models.TextField(default=None, null=True, blank=True)

    #def __str__(self):
        #return self.title()
