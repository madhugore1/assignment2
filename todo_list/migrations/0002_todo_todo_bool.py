# Generated by Django 2.2.1 on 2019-05-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_bool',
            field=models.BooleanField(default='True'),
        ),
    ]
