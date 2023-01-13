from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    opponent_username = models.CharField(max_length=15)
    opponent_username = models.CharField(max_length=15)
    chance = models.BooleanField(default=False)

class UserPieacePoses(models.Model):
    username = models.CharField(max_length=15)
    health = models.CharField(max_length=50,default='100.0')
    kar = models.CharField(max_length=10)
    kar2 =models.CharField(max_length=10)
    nade =models.CharField(max_length=10)
    nade2 = models.CharField(max_length=10)
    m24 = models.CharField(max_length=10)
    m242 =models.CharField(max_length=10)
    akm = models.CharField(max_length=10)
    akm2 =models.CharField(max_length=10)
    awm = models.CharField(max_length=10)
    m416 =models.CharField(max_length=10)
    shot1 =models.CharField(max_length=10)
    shot2 =models.CharField(max_length=10)
    shot3 =models.CharField(max_length=10)
    shot4 =models.CharField(max_length=10)
    shot5 =models.CharField(max_length=10)
    shot6 =models.CharField(max_length=10)
    shot7 =models.CharField(max_length=10)
    shot8 =models.CharField(max_length=10)
    shot9 =models.CharField(max_length=10)
    shot10 = models.CharField(max_length=10)