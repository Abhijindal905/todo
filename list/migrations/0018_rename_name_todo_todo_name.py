# Generated by Django 5.0.6 on 2024-11-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0017_alter_todo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='todo_name',
        ),
    ]
