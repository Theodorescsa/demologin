# Generated by Django 4.1 on 2023-03-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_member_department_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='department_id',
        ),
    ]
