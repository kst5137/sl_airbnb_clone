from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     phone = models.CharField(
#         max_length=100
#     )
#
#     # 회원 가입 시 이메일 입력을 필수로 한다.
#     REQUIRED_FIELDS = ["email"]

class User(AbstractUser):
    # u_id = models.CharField(max_length=200, verbose_name='아이디')  # user 아이디
    u_phonenum = models.CharField(max_length=200, verbose_name='전화번호', null=True)  # user 전화번호
    u_address = models.CharField(max_length=200, verbose_name='주소', null=True)  # user 주소
    SEX = (('F', '여자'), ('M', '남자'), ('U', '선택 안함'))
    u_sex = models.CharField(max_length=10, choices=SEX, null=True, unique=False)
