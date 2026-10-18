# models.py

from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,default=0)

    academicyear = models.CharField(max_length=20,default="2024-25")
    subject = models.CharField(max_length=20,default="C language")
    faculty = models.CharField(max_length=20,default="Rajeev kumar")
    course = models.CharField(max_length=20,default="computer science")
    semester = models.CharField(max_length=20,default="I")
    feedback_date = models.DateField(
    null=True,
    blank=True
)

    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3a = models.IntegerField(default=0)
    q3b = models.IntegerField(default=0)
    q3c = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'data'


    def __str__(self):
        return f"{self.student.username} - {self.subject}"
