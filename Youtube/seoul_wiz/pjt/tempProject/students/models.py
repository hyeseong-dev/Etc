from django.db import models    

class Student(models.Model):
    ''' Student 테이블을 생성'''
    s_name = models.CharField(max_length = 100)
    s_major = models.CharField(max_length = 100)
    s_age = models.IntegerField(default = 0)
    s_grade = models.IntegerField(default = 0)
    s_gender = models.CharField(max_length = 30)

    def __str__(self):
        return self.s_name
