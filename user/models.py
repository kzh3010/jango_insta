from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

# 커스텀한 유저 데이터
class User(AbstractBaseUser):
    '''
        유저 프로필 사진
        유저 아이디 => 닉네임 => 화면에 표기되는
        유저 이름 => 실제 사용자 이름
        유저 이메일 주소 => 회원가입할 때 사용하는 아이디
        비밀번호 => 디폴트 쓰자
    '''
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.CharField(unique=True, max_length=24)

    USERNAME_FIELD = "nickname"
    # 우리가 원하은 테이블 이름
    class Meta :
        db_table = "User"