# Generated by Django 4.2.3 on 2023-07-31 06:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpleapp', '0014_alter_news_amount_of_pages_alter_news_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='list_of_subscribtions',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 31, 15, 20, 23, 359728)),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]