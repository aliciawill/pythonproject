from django.db import models

# Create your models here.
class Test(models.Model): #테이블이름 Test
    # id는 자동생성
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ', ' + self.tel + ', ' + self.addr

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text