from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)
    author = models.ForeignKey(User,related_name = 'foodblog_food',on_delete=models.CASCADE)
    desc = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
