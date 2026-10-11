from django.db import models


class Feedback(models.Model):
    roleValue = models.CharField(max_length=30, blank=True)
    teacher = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    target = models.CharField(max_length=150, blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=50, blank=True)
    teaching = models.PositiveSmallIntegerField(null=True, blank=True)
    communication = models.PositiveSmallIntegerField(null=True, blank=True)
    support = models.PositiveSmallIntegerField(null=True, blank=True)
    growth = models.PositiveSmallIntegerField(null=True, blank=True)
    comment = models.TextField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'data'
