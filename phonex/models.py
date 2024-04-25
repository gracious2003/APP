from django.db import models

class Login(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length=255)

class Register(models.Model):
    username = models.CharField(max_length=20)
    
    email = models.CharField(max_length=255)
    
    password = models.CharField(max_length=255)




class sellphone(models.Model):
  phone_model = models.CharField(max_length=255)
  condition = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  decription= models.CharField(max_length=255)
  
class iphone(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class samsung(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class infinix(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class Tecno(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class itel(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class google_pixel(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class huawei(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class opoo(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

class redmi(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)


class sony(models.Model):
  phone_type = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
# Create your models here.
