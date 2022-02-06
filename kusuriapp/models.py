from distutils import text_file
from time import time
from turtle import update
from django.db import models

class UserModel (models.Model) :
  user_id = models.IntegerField()
  login_id = models.IntegerField()
  password = models.IntegerField()
  create_data = models.DateField()
  update_data = models.DateField()
  delete_data = models.DateField()

  class Medicine_Mangement(models.Model) :
    user_id = models.ForeignKey(on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=100)
    taking_dossage = models.IntegerField()
    taking_unit = models.IntegerField()
    taking_time = models.ForeignKey(user_id, on_delete=models.CASCADE)
    taking_start = models.DateTimeField()
    taking_end = models.DateTimeField()
    text = models.TextField()
  class Medicine_name_management(models.Model) :
    user_id = models.ForeignKey(on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
  
  class Medicine_Register(models.Model) :
    null = models.ForeignKey(user_id, on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    kinds = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=100)
    socienty = models.CharField(max_length=100)
  
  class taking_dosage(models.Model) :
    user_id = models.ForeignKey(null, on_delete=models.CASCADE)
    name = models.ForeignKey(user_id, on_delete=models.CASCADE)
    madicine =models.CharField(max_length=100)
    taking_dosage = models.IntegerField()
    taking_unit = models.IntegerField()
    taking_number = models.IntegerField()
  
  class taking_time_alarm(models.Model) :
    taking_time = models.TimeField

# Create your models here.
