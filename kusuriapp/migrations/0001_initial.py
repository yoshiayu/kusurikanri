# Generated by Django 4.0.2 on 2022-02-10 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kusuriapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('user_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='ユーザーID')),
                ('login_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='ログイン')),
                ('create_data', models.DateField()),
                ('update_data', models.DateField()),
                ('delete_data', models.DateField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', kusuriapp.models.UserModel()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineMangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='服用薬')),
                ('taking_dossage', models.IntegerField(blank=True, default=0, null=True, verbose_name='服用量')),
                ('taking_unit', models.IntegerField(blank=True, default=0, null=True, verbose_name='服用単位')),
                ('taking_start', models.DateTimeField(blank=True, default=-32400, null=True, verbose_name='服用開始')),
                ('taking_end', models.DateTimeField(blank=True, default=-32400, null=True, verbose_name='服用終了')),
                ('text', models.TextField(blank=True, max_length=1000, null=True, verbose_name='薬メモ')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineNameManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='服用者')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
        migrations.CreateModel(
            name='TakingTimeAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taking_time', models.ManyToManyField(to='kusuriapp.TakingTimeAlarm', verbose_name='服用時刻')),
            ],
        ),
        migrations.CreateModel(
            name='TakingDosage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taking_dosage', models.IntegerField(blank=True, default=0, null=True, verbose_name='服用量')),
                ('taking_unit', models.IntegerField(blank=True, default=0, null=True, verbose_name='服用単位')),
                ('taking_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='服用回数')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kusuriapp.medicinemangement', verbose_name='服用薬')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kusuriapp.medicinenamemanagement', verbose_name='服用者')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='種別')),
                ('dosage_form', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='剤型')),
                ('socienty', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='メーカー')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kusuriapp.medicinemangement', verbose_name='服用薬')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kusuriapp.medicinenamemanagement', verbose_name='服用者')),
            ],
        ),
        migrations.AddField(
            model_name='medicinemangement',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kusuriapp.medicinenamemanagement', verbose_name='服用者'),
        ),
        migrations.AddField(
            model_name='medicinemangement',
            name='taking_time',
            field=models.ManyToManyField(to='kusuriapp.TakingTimeAlarm', verbose_name='服用時刻'),
        ),
        migrations.AddField(
            model_name='medicinemangement',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID'),
        ),
    ]
