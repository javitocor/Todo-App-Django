from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.title