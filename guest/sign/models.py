from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)             #发布会标题
    limit = models.IntegerField()                       #参加人数
    stauts = models.BooleanField()                      #状态
    address = models.CharField(max_length=200)          #地址
    start_time = models.DateTimeField('event_time')     #发布会时间
    create_time = models.DateTimeField(auto_now=True)   #创建时间
        def __str__(self):
            return self.name