# models.py

from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    academic_year = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    semester = models.IntegerField()
    feedback_date = models.DateField()

    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3a = models.IntegerField()
    q3b = models.IntegerField()
    q3c = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Records'

    def __str__(self):
        return f"{self.student.username} - {self.subject}"
