# Generated by Django 4.0.4 on 2022-05-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_qualificationchecklist_title'),
        ('pipelines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelineworkflow',
            name='candidates',
            field=models.ManyToManyField(blank=True, to='candidates.candidate'),
        ),
    ]