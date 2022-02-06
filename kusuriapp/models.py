from distutils import text_files
from tabnanny import verbose
from time import time, timezone
from turtle import update
from wsgiref.validate import validator
from django.db import models

class UserModel (models.Model) :
  user_id = models.IntegerField(
    verbose_name='',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)]
  )
  login_id = models.IntegerField(verbose_name='',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
  password = models.IntegerField(verbose_name='',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
  create_data = models.DateField()
  update_data = models.DateField()
  delete_data = models.DateField()

  class Medicine_Mangement(models.Model) :
    user_id = models.ForeignKey(on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    medicine = models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
      )
    taking_dossage = models.IntegerField(verbose_name='',
      blank=True,
      null=True,
      default=0,
      validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    taking_unit = models.IntegerField(verbose_name='',
      blank=True,
      null=True,
      default=0,
      validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    taking_time = models.ForeignKey(user_id, on_delete=models.CASCADE)
    taking_start = models.DateTimeField(
      verbose_name='',
      blank=True,
      null=True,
      default=timezone.now
    )
    taking_end = models.DateTimeField(
      verbose_name='',
      blank=True,
      null=True,
      default=timezone.now
    )
    text = models.TextField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=1000,
    )
  class Medicine_name_management(models.Model) :
    user_id = models.ForeignKey(on_delete=models.CASCADE)
    name = models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
    )
  
  class Medicine_Register(models.Model) :
    verbose_name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    kinds = models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
    )
    dosage_form = models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
    )
    socienty = models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
    )
  
  class taking_dosage(models.Model) :
    user_id = models.ForeignKey(null, on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    madicine =models.CharField(
      verbose_name='',
      blank=True,
      null=True,
      max_length=50,
      default='',
      validators=[validators.RegexValidator(
        regex=u'[ぁｰんァ-ヶ]+$',
        massage='全角のひらがな・カタカナ・漢字で入力してください',
      )]
    )
    taking_dosage = models.IntegerField(verbose_name='',
      blank=True,
      null=True,
      default=0,
      validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    taking_unit = models.IntegerField(verbose_name='',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    taking_number = models.IntegerField(verbose_name='',
      blank=True,
      null=True,
      default=0,
      validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
  
  class taking_time_alarm(models.Model) :
    taking_time = models.TimeField

# Create your models here.
