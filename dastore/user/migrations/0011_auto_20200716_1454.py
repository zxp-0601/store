# Generated by Django 2.2.12 on 2020-07-16 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200716_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.date(1900, 1, 1), null=True, verbose_name='生日'),
        ),
    ]
