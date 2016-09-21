from django.db import models

# Create your models here.
import datetime

class ProfilePics(models.Model):
	username = models.CharField(max_length=50)
	profilepic = models.CharField(max_length=255, default='users/avatar.jpg')
	timestamp = models.DateField('', default=datetime.date.today)

	class Meta:
		db_table = "ProfilePics"