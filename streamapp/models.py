from django.db import models
from django.utils import timezone
# Create your models here.

class Cam(models.Model):
    cam_name = models.CharField(max_length = 40,default="My Cam")
    timestamp = models.DateTimeField(default=timezone.now)
    framecount = models.IntegerField(default=0)
    is_webcam = models.BooleanField(null=False)
