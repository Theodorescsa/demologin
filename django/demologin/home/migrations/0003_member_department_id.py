# Generated by Django 4.1 on 2023-03-11 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='department_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
    ]