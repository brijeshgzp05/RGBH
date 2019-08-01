from django.db import models

# Create your models here.
class Post(models.Model):
	post_type = models.CharField(max_length=50)

	def __str__(self):
		return self.post_type

class Staff(models.Model):
	name = models.CharField(max_length=50)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	salary = models.IntegerField()
	mobile = models.CharField(max_length=10, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	address = models.CharField(max_length=200)
	timestamp = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']


