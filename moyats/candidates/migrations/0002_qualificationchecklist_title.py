# Generated by Django 4.0.4 on 2022-05-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualificationchecklist',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]