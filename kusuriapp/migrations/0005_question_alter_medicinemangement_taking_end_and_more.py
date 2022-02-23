# Generated by Django 4.0.2 on 2022-02-23 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kusuriapp', '0004_alter_companymedicinename_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 19, 17, 56, 277686), null=True, verbose_name='服用終了'),
        ),
        migrations.AlterField(
            model_name='medicinemangement',
            name='taking_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 19, 17, 56, 277674), null=True, verbose_name='服用開始'),
        ),
    ]
