# Generated by Django 2.0.2 on 2018-03-23 12:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180320_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='datepulished',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 12, 35, 28, 692680, tzinfo=utc)),
        ),
    ]
