from django.db import models

# Create your models here.
class Timing(models.Model):
	breakfast_time = models.CharField(max_length=30)
	lunch_time = models.CharField(max_length=30)
	evening_time = models.CharField(max_length=30)
	dinner_time = models.CharField(max_length=30)

class Item(models.Model):
	day = models.CharField(max_length=20, null=True, blank=True)
	breakfast = models.CharField(max_length=200)
	lunch = models.CharField(max_length=200)
	evening = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)
	updated = models.DateField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.day
