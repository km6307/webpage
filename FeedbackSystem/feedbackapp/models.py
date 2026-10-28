from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    academicyear = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    feedback_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    

    # q1 = models.IntegerField()
    # q2 = models.IntegerField()
    # q3a = models.IntegerField()
    # q3b = models.IntegerField()
    # q3c = models.IntegerField()
    # q4 = models.IntegerField()
    # q5 = models.IntegerField()
    # q6 = models.IntegerField()

    class Meta:
        db_table = 'data'