# Generated by Django 4.0.4 on 2022-05-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0004_alter_pipelinesetup_triggers'),
        ('joborders', '0002_alter_jobdetail_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='joborder',
            name='job_order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pipelines.pipelinestatus'),
        ),
    ]