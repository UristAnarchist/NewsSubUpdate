# Generated by Django 4.2.3 on 2023-07-27 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0009_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 27, 20, 8, 39, 593514)),
        ),
    ]