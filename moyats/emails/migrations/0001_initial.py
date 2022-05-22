# Generated by Django 4.0.4 on 2022-05-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opens', models.BigIntegerField(default=0)),
                ('clicks', models.BigIntegerField(default=0)),
                ('bounces', models.BigIntegerField(default=0)),
                ('unsubscribes', models.BigIntegerField(default=0)),
                ('spam', models.BigIntegerField(default=0)),
                ('open_rate', models.CharField(max_length=200)),
                ('click_rate', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('op', 'Opened'), ('cl', 'Clicked'), ('bo', 'Bounced'), ('us', 'Unsubscribed'), ('ms', 'Marked Spam')], max_length=2)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('co', 'Contact'), ('ca', 'Candidate'), ('cd', 'Custom Detail')], max_length=2)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emails.emailreport')),
            ],
        ),
        migrations.CreateModel(
            name='CoreEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('signiture', models.TextField()),
                ('schedule', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.emailrecipient')),
            ],
        ),
    ]
