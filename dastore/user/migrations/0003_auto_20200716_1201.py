# Generated by Django 2.2.12 on 2020-07-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200715_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default='', verbose_name='生日'),
        ),
    ]