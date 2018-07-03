from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# 为了和数据库进行交互
# 一个类表示一个表；类的每个实例表示一行，每个变量表示一个字段
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published') # 算是comment？

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now=timezone.now()
        return now>=self.pub_date>=now-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

