# Generated by Django 2.2.12 on 2020-07-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200716_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(verbose_name='生日'),
        ),
    ]
