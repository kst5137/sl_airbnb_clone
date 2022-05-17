from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    u_id = models.CharField(max_length=200, verbose_name='아이디')  # user 아이디
    u_phonenum = models.CharField(max_length=200, verbose_name='전화번호')  # user 전화번호
    u_address = models.CharField(max_length=200, verbose_name='주소')  # user 주소
