# Generated by Django 3.1.6 on 2021-02-10 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='article',
            new_name='table',
        ),
    ]
