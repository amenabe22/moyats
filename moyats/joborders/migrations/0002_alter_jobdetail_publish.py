# Generated by Django 4.0.4 on 2022-05-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joborders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='publish',
            field=models.BooleanField(default=True, help_text='publish job order on publish status change'),
        ),
    ]
