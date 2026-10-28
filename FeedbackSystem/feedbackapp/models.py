# models.py

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


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
    average_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ratings = [self.q1, self.q2, self.q3a, self.q3b, self.q3c, self.q4, self.q5, self.q6]
        self.average_rating = (Decimal(sum(ratings)) / Decimal(len(ratings))).quantize(Decimal("0.01"))
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'data'

#######################data base me data name se table create hoga
    def __str__(self):
        return f"{self.student.username} - {self.subject}"
