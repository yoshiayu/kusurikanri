from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from time import timezone
from time import time 
from django.contrib.auth.base_user import BaseUserManager

def get_upload_file_name(filename):
    return  "uploaded_files/%s_%s" % (str(time()).replace(".", "_"), filename)
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

class User(AbstractBaseUser, PermissionsMixin) :
   
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
        help_text=('Designates whether this user should be treated as active.' 'Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    objects = UserModel()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.first_name
    
    def __str__(self):
        return self.last_name
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
class MedicineNameManagement(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.CharField(
        verbose_name='服用者',
        blank=True,
        null=True,
        max_length=50,
        default='',
    ) 
class MedicineMangement(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.CharField(
        verbose_name='服用薬',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
    taking_dossage = models.IntegerField(verbose_name='服用量',
        blank=True,
        null=True,
        default=0,
    )
    taking_unit = models.IntegerField(verbose_name='服用単位',
        blank=True,
        null=True,
        default=0,
    )
    taking_time = models.ManyToManyField('TakingTimeAlarm', verbose_name='服用時刻')
    taking_start = models.DateTimeField(
        verbose_name='服用開始',
        blank=True,
        null=True,
        default=timezone
    )
    taking_end = models.DateTimeField(
        verbose_name='服用終了',
        blank=True,
        null=True,
        default=timezone
    )
    text = models.TextField(
        verbose_name='薬メモ',
        blank=True,
        null=True,
        max_length=1000,
    )
class MedicineRegister(models.Model) :
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(MedicineMangement, on_delete=models.CASCADE, verbose_name='服用薬')  
    kinds = models.CharField(
        verbose_name='種別',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
    dosage_form = models.CharField(
        verbose_name='剤型',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
    socienty = models.CharField(
        verbose_name='メーカー',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
class TakingDosage(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(MedicineMangement, on_delete=models.CASCADE, verbose_name='服用薬')  
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
class TakingTimeAlarm(models.Model) :
    taking_time = models.ManyToManyField('TakingTimeAlarm', verbose_name='服用時刻')

# Create your models here.
