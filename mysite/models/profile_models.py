from django.db import models

class Profile(models.Model):
	username   = models.CharField(default="匿名ユーザー", max_length=30)
	zipcode    = models.CharField(default="", max_length=8)
	prefecture = models.CharField(default="", max_length=6)
	city       = models.CharField(default="", max_length=50)
	address    = models.CharField(default="", max_length=200)
