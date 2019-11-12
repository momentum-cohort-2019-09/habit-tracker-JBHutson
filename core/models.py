from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None)
    target = models.IntegerField()
    user = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user'
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    end_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class HabitRecord(models.Model):
    record = models.TextField()
    actual_num_achieved = models.IntegerField(default=None)
    met_goal = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    habit = models.ForeignKey(
        to = Habit,
        on_delete = models.CASCADE,
        related_name = 'habit_record_is_for'
    )

    def __str__(self):
        return self.record

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

    def __str__(self):
        return self.comment

class HabitObserver(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user_observing_habit'
    )
    habit_observing = models.ForeignKey(
        to=Habit,
        on_delete= models.CASCADE,
        related_name='habbit_record_observing'
    )
    started_observing_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.habit_observing.__str__()

class UserObserving(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user_observing_user'
    )
    user_observe = models.ForeignKey(
        to=User,
        on_delete= models.CASCADE,
        related_name='user_observed'
    )
    started_observing_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user_observe.__str__()