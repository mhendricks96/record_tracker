from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Record(models.Model):
  title = models.CharField(max_length=64)
  artist = models.CharField(max_length=64)
  genre = models.CharField(max_length=64)
  #date_added = models.DateTimeField(auto_now_add=True)
  added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('record_detail', args=[str(self.id)])
