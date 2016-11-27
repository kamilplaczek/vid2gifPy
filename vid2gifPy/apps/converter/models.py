from django.db import models


# Create your models here.
class ConvertVidRequestModel(models.Model):
    is_loop = models.BooleanField()
    vid_file = models.FileField(upload_to="uploads/%Y/%m")
