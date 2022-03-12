import datetime
from tabnanny import verbose
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from time import time
from django.contrib.auth.base_user import BaseUserManager


class Question(models.Model):
    pass


def get_upload_file_name(filename):
    return "uploaded_files/%s_%s" % (str(time()).replace(".", "_"), filename)


class UserModel(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active.' 'Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)

    objects = UserModel()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    user_id = models.IntegerField(
        verbose_name='ユーザーID',
        blank=True,
        null=True,
        default=0,
    )
    login_id = models.IntegerField(
        verbose_name='ログイン',
        blank=True,
        null=True,
        default=0,
    )
    create_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)
    delete_data = models.DateField(default=None, null=True, blank=True)


class MedicineNameManagement(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.CharField(
        verbose_name='服用者',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )

    def __str__(self):
        return self.name


TAKING_UNIT = (
    ('0', '錠'),
    ('1', '包'),
    ('2', '滴'),
    ('3', 'mg'),
    ('4', 'ml'),
)
TAKING_TIME = (
    ('0', '朝'),
    ('1', '昼'),
    ('2', '夕'),
    ('3', '寝る前'),
    ('4', '朝食前'),
    ('5', '昼食前'),
    ('6', '夕食前'),
    ('7', '朝食後'),
    ('8', '昼食後'),
    ('9', '夕食後'),
    ('10', '食間（朝昼）'),
    ('11', '食間（昼夕）'),
)


class MedicineMangement(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement,
                             on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(
        'MedicineRegister', on_delete=models.CASCADE, default=None, verbose_name='服用薬')
    taking_dossage = models.IntegerField(verbose_name='服用量',
                                         blank=True,
                                         null=True,
                                         default=0,
                                         )
    taking_unit = models.IntegerField(verbose_name='服用単位',
                                      blank=True,
                                      null=True,
                                      default=0,
                                      choices=TAKING_UNIT
                                      )
    taking_time = models.ManyToManyField(
        'TakingTimeAlarm', verbose_name='服用時刻')
    taking_start = models.DateTimeField(
        verbose_name='服用開始',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )

    def __str__(self):
        return self.taking_start

    taking_end = models.DateTimeField(
        verbose_name='服用終了',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )

    def __str__(self):
        return self.taking_end

    text = models.TextField(
        verbose_name='薬メモ',
        blank=True,
        null=True,
        max_length=1000,
    )


KINDS_LIST = (
    ('0', '処方'),
    ('1', '処方（ジェネリック）'),
    ('2', '処方（漢方）'),
    ('3', '市販薬'),
    ('4', '市販薬（子供用）'),
    ('5', 'セルフメディケーション税剤対象'),
)
DOSAGE_FORM = (
    ('0', '散剤'),
    ('1', '錠剤'),
    ('2', 'カプセル'),
    ('3', '液剤'),
    ('4', '外用薬'),
    ('5', '注射剤'),
    ('6', '自己注射剤'),
    ('7', 'その他'),
)


class MedicineRegister(models.Model):
    name = models.ForeignKey(MedicineNameManagement,
                             on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(
        'CompanyMedicineName', on_delete=models.CASCADE, verbose_name='服用薬', blank=True, null=True, default=1)

    # def __str__(self):
    #    return self.medicine('CompanyMedicineName')

    kinds = models.CharField(
        verbose_name='種別',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=KINDS_LIST
    )
    # def __str__(self):
    #    return self.kinds

    dosage_form = models.CharField(
        verbose_name='剤型',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=DOSAGE_FORM
    )
    # def __str__(self):
    #    return self.dosage_form

    # socienty = models.CharField(
    #    verbose_name='メーカー',
    #    blank=True,
    #    null=True,
    #    max_length=50,
    #    default='',
    #    choices=COMPANY_LIST
    # )


class TakingDosage(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement,
                             on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(
        MedicineMangement, on_delete=models.CASCADE, verbose_name='服用薬')
    taking_dosage = models.IntegerField(
        verbose_name='服用量',
        blank=True,
        null=True,
        default=0,
    )
    taking_unit = models.IntegerField(
        verbose_name='服用単位',
        blank=True,
        null=True,
        default=0,
    )
    taking_number = models.IntegerField(
        verbose_name='服用回数',
        blank=True,
        null=True,
        default=0,
    )


class TakingTimeAlarm(models.Model):
    taking_time = models.TimeField(default=None, verbose_name='服用時刻')

    def __str__(self):
        return str(self.taking_time)


class CompanyMedicineName(models.Model):
    company_id = models.IntegerField(
        verbose_name='会社ID', blank=True, null=True)
    company_name = models.CharField(
        max_length=20, verbose_name='会社名', blank=True, null=True)
    medicine_id = models.IntegerField(
        verbose_name='薬ID', blank=True, null=True)
    medicine_name = models.CharField(
        max_length=30, verbose_name='薬名', blank=True, null=True)
    initials = models.CharField(
        max_length=1, verbose_name='頭文字', blank=True, null=True)

    class Meta:
        verbose_name_plural = '薬及び会社リスト'

    def __str__(self):
        return self.medicine_name

    # サンプル項目1 日付


class Item(models.Model):

    sample_1 = models.DateField(
        verbose_name='サンプル項目1 日付',
        blank=True,
        null=True,
    )

    # サンプル項目2 日付時刻
    sample_2 = models.DateTimeField(
        verbose_name='サンプル項目2 日付時刻',
        blank=True,
        null=True,
    )

    # サンプル項目3 時刻
    sample_3 = models.TimeField(
        verbose_name='サンプル項目3 日時',
        blank=True,
        null=True,
    )

    # サンプル項目4 期間 開始日
    sample_4_start = models.DateField(
        verbose_name='サンプル項目4 期間 開始日',
        blank=True,
        null=True,
    )

    # サンプル項目4 期間 終了日
    sample_4_end = models.DateField(
        verbose_name='サンプル項目4 期間 終了日',
        blank=True,
        null=True,
    )
