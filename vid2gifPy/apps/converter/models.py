from django.db import models
from enum import IntEnum

class LoopMode(IntEnum):
    regular = 1,
    symmetrical = 2

class Size(IntEnum):
    original = 1
    smaller = 2
    bigger = 3

class CaptionPosition(IntEnum):
    top = 1,
    middle = 2,
    bottom = 3

class Quality(IntEnum):
    regular = 1
    high = 2
    low = 3

class Speed(IntEnum):
    normal = 1
    fast = 2
    slow = 3

# Create your models here.
class ConvertVidRequestModel(models.Model):
    LOOP_MODE_CHOICES = (
        (LoopMode.regular.value, 'Regular'),
        (LoopMode.symmetrical.value, 'Symmetrical')
    )
    SIZE_CHOICES = (
        (Size.original.value, 'Original'),
        (Size.smaller.value, 'Smaller'),
        (Size.bigger.value, 'Bigger')
    )
    CAPTION_POSITION_CHOICES = (
        (CaptionPosition.top.value, 'Top'),
        (CaptionPosition.middle.value, 'Middle'),
        (CaptionPosition.bottom.value, 'Bottom')
    )
    QUALITY_CHOICES = (
        (Quality.regular.value, 'Regular'),
        (Quality.high.value, 'High'),
        (Quality.low.value, 'Low')
    )
    SPEED_CHOICES = (
        (Speed.normal.value, 'Normal'),
        (Speed.fast.value, 'Fast'),
        (Speed.slow.value, 'Slow')
    )
    creation_date = models.DateField()
    loop_mode = models.IntegerField(default = 1, choices = LOOP_MODE_CHOICES)
    size = models.IntegerField(default = 1, choices = SIZE_CHOICES)
    speed = models.IntegerField(default = 1, choices = SPEED_CHOICES)
    quality = models.IntegerField(default = 1, choices = QUALITY_CHOICES)
    caption_position = models.IntegerField(default = 1, choices = CAPTION_POSITION_CHOICES)
    caption = models.CharField(max_length=50, null = True, blank = True)
    vid_file = models.FileField(upload_to="uploads/%Y/%m")
    result_file_name = models.CharField(max_length=50, null = True);
