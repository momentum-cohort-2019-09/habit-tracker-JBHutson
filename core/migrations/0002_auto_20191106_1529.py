# Generated by Django 2.2.2 on 2019-11-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='habit',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='habitrecord',
            name='actual_num_achieved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habitrecord',
            name='met_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='target',
            field=models.IntegerField(),
        ),
    ]
