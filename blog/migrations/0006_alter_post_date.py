# Generated by Django 5.1 on 2024-10-06 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 6, 14, 27, 58, 985277, tzinfo=datetime.timezone.utc)),
        ),
    ]
