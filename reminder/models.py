from django.db import models


class Reminder(models.Model):
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    

    def __str__(self):
        return self.title

    