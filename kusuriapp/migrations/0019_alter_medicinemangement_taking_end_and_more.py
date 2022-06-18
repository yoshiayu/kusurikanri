# Generated by Django 4.0.2 on 2022-06-18 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kusuriapp', '0018_alter_medicinemangement_taking_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 18, 17, 17, 137033), null=True, verbose_name='服用終了'),
        ),
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 18, 17, 17, 137021), null=True, verbose_name='服用開始'),
        ),
    ]
