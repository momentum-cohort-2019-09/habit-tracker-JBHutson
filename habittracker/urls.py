from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from core import api
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    path('', views.HomeView, name='home'),
    path('core/profile/<str:username>/', views.ProfileView, name='profile'),

    path('api/core/habits/', api.Habits.as_view()),
    path('api/core/habits_by_user/<str:username>/', api.HabitsByUser.as_view()),
    path('api/core/records_by_habit/<int:habit_id>/', api.HabitRecordsByHabit.as_view()),
    path('api/core/comments_by_habit_record/<int:habit_record_id>/', api.CommentsByHabit.as_view()),
    path('api/core/habits_observed_by_user/<str:username>/', api.HabitsObservedByUser.as_view()),
    path('api/core/users_observed_by_user/<str:username>/', api.UsersObservedByUser.as_view())
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
