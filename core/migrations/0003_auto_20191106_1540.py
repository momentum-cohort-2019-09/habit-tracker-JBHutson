# Generated by Django 2.2.2 on 2019-11-06 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191106_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitObserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_observing_at', models.DateField(default=django.utils.timezone.now)),
                ('habit_observing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habbit_record_observing', to='core.HabitRecord')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_observing_habit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserObserving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_observing_at', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_observing_user', to=settings.AUTH_USER_MODEL)),
                ('user_observe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_observed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Observer',
        ),
    ]
