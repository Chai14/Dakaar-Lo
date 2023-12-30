from django.db import models

class Chinese(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    chinese_icon = models.ImageField(upload_to="imgs/", default=None)
    chinese_name = models.CharField(max_length=50, default=None)
    chinese_price = models.CharField(max_length=50, default=None)
    chinese_des = models.TextField()

class Italian(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    italian_icon = models.ImageField(upload_to="imgs/", default=None)
    italian_name = models.CharField(max_length=50, default=None)
    italian_price = models.CharField(max_length=50, default=None)
    italian_des = models.TextField()

class Indian_Street(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    street_icon = models.ImageField(upload_to="imgs/", default=None)
    street_name = models.CharField(max_length=50, default=None)
    street_price = models.CharField(max_length=50, default=None)
    street_des = models.TextField()

class North(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    north_icon = models.ImageField(upload_to="imgs/", default=None)
    north_name = models.CharField(max_length=50, default=None)
    north_price = models.CharField(max_length=50, default=None)
    north_des = models.TextField()

class South(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    south_icon = models.ImageField(upload_to="imgs/", default=None)
    south_name = models.CharField(max_length=50, default=None)
    south_price = models.CharField(max_length=50, default=None)
    south_des = models.TextField()

class Guj(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    gujraj_icon = models.ImageField(upload_to="imgs/", default=None)
    gujraj_name = models.CharField(max_length=50, default=None)
    gujraj_price = models.CharField(max_length=50, default=None)
    gujraj_des = models.TextField()

class Custom(models.Model):
    demo = models.CharField(max_length=500, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Registration(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)

