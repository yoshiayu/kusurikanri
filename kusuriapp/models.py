"""_summary_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
"""
import datetime
from unicodedata import name
import schedule
from tabnanny import verbose
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from time import time
from django.contrib.auth.base_user import BaseUserManager


class Question(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    pass


def get_upload_file_name(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    return "uploaded_files/%s_%s" % (str(time()).replace(".", "_"), filename)


def job():
    print(datetime.datetime.now())
    print("I'm taking...")
    schedule.every().day.at("20:56").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)


class UserModel(BaseUserManager):
    """_summary_

    Args:
        BaseUserManager (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """_summary_

    Args:
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """
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
        verbose_name='????????????ID',
        blank=True,
        null=True,
        default=0,
    )
    login_id = models.IntegerField(
        verbose_name='????????????',
        blank=True,
        null=True,
        default=0,
    )
    create_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)
    delete_data = models.DateField(default=None, null=True, blank=True)


class MedicineNameManagement(models.Model):

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='????????????ID')
    name = models.CharField(
        verbose_name='?????????',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )

    def __str__(self):
        return self.name


TAKING_UNIT = (
    ('0', '???'),
    ('1', '???'),
    ('2', '???'),
    ('3', 'mg'),
    ('4', 'ml'),
)
TAKING_TIME = (
    ('0', '???'),
    ('1', '???'),
    ('2', '???'),
    ('3', '?????????'),
    ('4', '?????????'),
    ('5', '?????????'),
    ('6', '?????????'),
    ('7', '?????????'),
    ('8', '?????????'),
    ('9', '?????????'),
    ('10', '??????????????????'),
    ('11', '??????????????????'),
)


class MedicineMangement(models.Model):

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='????????????ID')
    name = models.ForeignKey(MedicineNameManagement,
                             on_delete=models.CASCADE, verbose_name='?????????')
    medicine = models.ForeignKey(
        'MedicineRegister', on_delete=models.CASCADE, default=None, verbose_name='?????????')
    taking_dossage = models.IntegerField(verbose_name='?????????',
                                         blank=True,
                                         null=True,
                                         default=0,
                                         )
    taking_unit = models.IntegerField(verbose_name='????????????',
                                      blank=True,
                                      null=True,
                                      default=0,
                                      choices=TAKING_UNIT
                                      )
    taking_time = models.ManyToManyField(
        'TakingTimeAlarm', verbose_name='????????????')
    taking_start = models.DateTimeField(
        verbose_name='????????????',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )

    # def __str__(self):
    #    return self.taking_start

    taking_end = models.DateTimeField(
        verbose_name='????????????',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )

    # def __str__(self):
    #    return self.taking_end

    text = models.TextField(
        verbose_name='?????????',
        blank=True,
        null=True,
        max_length=1000,
    )


KINDS_LIST = (
    ('0', '??????'),
    ('1', '??????????????????????????????'),
    ('2', '??????????????????'),
    ('3', '?????????'),
    ('4', '????????????????????????'),
    ('5', '?????????????????????????????????????????????'),
)
DOSAGE_FORM = (
    ('0', '??????'),
    ('1', '??????'),
    ('2', '????????????'),
    ('3', '??????'),
    ('4', '?????????'),
    ('5', '?????????'),
    ('6', '???????????????'),
    ('7', '?????????'),
)


class MedicineRegister(models.Model):

    # '''
    # name = models.ForeignKey(MedicineNameManagement,
    #                         on_delete=models.CASCADE, verbose_name='?????????')
    # '''

    medicine = models.ForeignKey(
        'CompanyMedicineName', on_delete=models.CASCADE, verbose_name='?????????', blank=True, null=True, default=1)

    # def __init__(self, medicine):
    #    self.medicine = medicine
    #self.medicine_name = name

    # def __repr__(self):
    #    return str(self.medicine.medicine_name)

    # def __str__(self):
    #    return str(self.medicine.medicine_name)
    # return str('{}.format(self.medicine.medicine_name)')
    #    return str(format(self.medicine.medicine_name))
    # self.medicine(self)
    # return str(self.medicine)
    # myMedicine = "Medicine: {}".format(self.medicine)
    # return myMedicine

    # def medicine(self):
    # self.medicine(self)
    # return self.medicine
    # return f'self.medicine'
    # return str(self.medicine.medicine_name)
    # return self.medicine.medicine_name

    kinds = models.CharField(
        verbose_name='??????',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=KINDS_LIST
    )
    # def __str__(self):
    #    return self.kinds

    dosage_form = models.CharField(
        verbose_name='??????',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=DOSAGE_FORM
    )
    # def __str__(self):
    #    return self.dosage_form

    # socienty = models.CharField(
    #    verbose_name='????????????',
    #    blank=True,
    #    null=True,
    #    max_length=50,
    #    default='',
    #    choices=COMPANY_LIST
    # )

    def __str__(self):
        return str(self.medicine.medicine_name)


class TakingDosage(models.Model):

    # user_id = models.ForeignKey(
    #    User, on_delete=models.CASCADE, verbose_name='????????????ID')
    # name = models.ForeignKey(MedicineNameManagement,
    #                          on_delete=models.CASCADE, verbose_name='?????????')
    name = models.CharField(max_length=50, verbose_name='?????????')
    medicine = models.ForeignKey(
        MedicineRegister, on_delete=models.CASCADE, verbose_name='?????????')

    def __str__(self):
        return f'{self.name} x {self.medicine}'

    # taking_dosage = models.IntegerField(
    #    verbose_name='?????????',
    #    blank=True,
    #    null=True,
    #    default=0,
    # )
    # taking_unit = models.IntegerField(
    #    verbose_name='????????????',
    #    blank=True,
    #    null=True,
    #    default=0,
    # )
    # taking_number = models.IntegerField(
    #    verbose_name='????????????',
    #    blank=True,
    #    null=True,
    #    default=0,
    # )


class TakingTimeAlarm(models.Model):
    taking_time = models.TimeField(default=None, verbose_name='????????????')

    def __str__(self):
        return str(self.taking_time)


class CompanyMedicineName(models.Model):
    company_id = models.IntegerField(
        verbose_name='??????ID', blank=True, null=True)
    company_name = models.CharField(
        max_length=20, verbose_name='?????????', blank=True, null=True)
    medicine_id = models.IntegerField(
        verbose_name='???ID', blank=True, null=True)
    medicine_name = models.CharField(unique=True,
                                     max_length=30, verbose_name='??????', blank=True, null=True)
    initials = models.CharField(
        max_length=1, verbose_name='?????????', blank=True, null=True)

    class Meta:
        verbose_name_plural = '????????????????????????'

    def __str__(self):
        return f'{self.medicine_name}({self.company_name})'

    # def __str__(self):
    #    return str(self.medicine_name)

    # def __str__(self):
    #     return str(self.company_name)

    # ??????????????????1 ??????


class Item(models.Model):

    sample_1 = models.DateField(
        verbose_name='??????????????????1 ??????',
        blank=True,
        null=True,
    )

    # ??????????????????2 ????????????
    sample_2 = models.DateTimeField(
        verbose_name='??????????????????2 ????????????',
        blank=True,
        null=True,
    )

    # ??????????????????3 ??????
    sample_3 = models.TimeField(
        verbose_name='??????????????????3 ??????',
        blank=True,
        null=True,
    )

    # ??????????????????4 ?????? ?????????
    sample_4_start = models.DateField(
        verbose_name='??????????????????4 ?????? ?????????',
        blank=True,
        null=True,
    )

    # ??????????????????4 ?????? ?????????
    sample_4_end = models.DateField(
        verbose_name='??????????????????4 ?????? ?????????',
        blank=True,
        null=True,
    )
