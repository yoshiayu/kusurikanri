# Generated by Django 4.0.2 on 2022-04-03 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kusuriapp', '0014_remove_medicineregister_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 3, 20, 4, 24, 973831), null=True, verbose_name='服用終了'),
        ),
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 3, 20, 4, 24, 973821), null=True, verbose_name='服用開始'),
        ),
    ]
