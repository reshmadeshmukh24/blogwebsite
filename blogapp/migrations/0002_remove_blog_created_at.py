# Generated by Django 3.2.2 on 2021-05-30 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
    ]
