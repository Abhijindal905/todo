# Generated by Django 5.0.6 on 2024-11-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_alter_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
