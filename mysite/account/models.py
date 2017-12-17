from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):    #建立名为account_userprofile的数据库表
    user = models.OneToOneField(User, unique=True)  #通过user字段，声明UserProfile类与User类的关系为"一对一"
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
