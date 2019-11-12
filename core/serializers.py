from rest_framework import serializers
from core.models import User, Habit, HabitRecord, Comment, HabitObserver

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'name', 'description', 'target', 'created_at', 'updated_at', 'end_date']

class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = ['id', 'record', 'actual_num_achieved', 'met_goal', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'updated_at']