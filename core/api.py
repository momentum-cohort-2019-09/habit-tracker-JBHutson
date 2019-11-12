from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import User, Habit, HabitRecord, Comment, HabitObserver, UserObserving
from core.serializers import UserSerializer, HabitSerializer, HabitRecordSerializer, CommentSerializer

class Habits(APIView):

    def get(self, request, format=None):
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

class HabitsByUser(APIView):

    def get(self, request, username, format=None):
        habits = Habit.objects.filter(user=User.objects.get(username=username))
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

class HabitRecordsByHabit(APIView):

    def get(self, request, habit_id, fromat=None):
        habit_records = HabitRecord.objects.filter(habit=Habit.objects.get(id=habit_id))
        serializer = HabitRecordSerializer(habit_records, many=True)
        return Response(serializer.data)

class CommentsByHabit(APIView):

    def get(self, request, habit_record_id, format=None):
        comments = Comment.objects.filter(habit_record=HabitRecord.objects.get(id=habit_record_id))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class HabitsObservedByUser(APIView):

    def get(self, request, username, format=None):
        observed_habits = Habit.objects.filter(pk__in=HabitObserver.objects.filter(user=User.objects.get(username=username)).values_list("habit_observing", flat=True))
        serializer = HabitSerializer(observed_habits, many=True)
        return Response(serializer.data)

class UsersObservedByUser(APIView):

    def get(self, request, username, format=None):
        observed_users = User.objects.filter(pk__in=UserObserving.objects.filter(user=User.objects.get(username=username)).values_list("user_observe", flat=True))
        serializer = UserSerializer(observed_users, many=True)
        return Response(serializer.data)