# Generated by Django 4.0.4 on 2022-05-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0004_alter_pipelinesetup_triggers'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipelineworkflow',
            name='workflow_status',
            field=models.ManyToManyField(blank=True, to='pipelines.pipelinestatus'),
        ),
    ]
