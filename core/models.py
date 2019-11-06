from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.email


class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    user = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user'
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

class HabitRecord(models.Model):
    record = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

class Comment(models.Model):
    user_making = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user_making'
    )
    comment = models.TextField()
    habit_record = models.ForeignKey(
        to=HabitRecord,
        on_delete= models.CASCADE,
        related_name='habit_record'
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

class Observer(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user_observing'
    )
    habit_observing = models.ForeignKey(
        to=HabitRecord,
        on_delete= models.CASCADE,
        related_name='habbit_record_observing'
    )
    started_observing_at = models.DateField(default=timezone.now)