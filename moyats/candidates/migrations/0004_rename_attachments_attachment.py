# Generated by Django 4.0.4 on 2022-05-22 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_rename_socialmedias_socialmedia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attachments',
            new_name='Attachment',
        ),
    ]
