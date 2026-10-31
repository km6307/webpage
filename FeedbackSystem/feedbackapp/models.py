from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    academicYear = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    facultyName = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    feedbackDate = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0.0)

    class Meta:
     db_table = 'data'
     unique_together = ('student', 'academicYear', 'semester', 'subject', 'facultyName')