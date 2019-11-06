from django.contrib import admin
from core.models import User, Habit, HabitRecord, Comment, Observer
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(HabitRecord)
admin.site.register(Comment)
admin.site.register(Observer)
