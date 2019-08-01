from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Student(models.Model):

	name = models.CharField(max_length=50)
	rollno = models.CharField(max_length=11,null=True, blank=True)
	slug = models.SlugField(unique=True, null=True)
	dob = models.DateField()
	branch = models.CharField(max_length=50)
	# session = models.CharField(max_length=10)
	gender = models.CharField(max_length=6)
	aadhar = models.CharField(max_length=12, null=True, blank=True)
	mobile = models.CharField(max_length=10)
	fees_paid = models.IntegerField()
	pending_fees = models.IntegerField(null=True, blank=True)
	fully_paid = models.BooleanField(default=False)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	year = models.IntegerField()
	roomno = models.CharField(max_length=5,null=True, blank=True)
	bedno = models.CharField(max_length=2,null=True, blank=True)
	timestamp = models.DateField(auto_now=False,auto_now_add=True)
	updated = models.DateField(auto_now_add=False,auto_now=True)
	
	def get_absolute_url(self):
		return reverse('students:detail', kwargs={'slug':self.slug})

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug=new_slug
	qs=Student.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_student_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

pre_save.connect(pre_save_student_receiver, sender=Student)