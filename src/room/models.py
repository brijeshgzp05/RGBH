from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


TYPE_CHOICES = (
    ('ac','AC'),
    ('non-ac', 'NON-AC'),
    
)

class Room(models.Model):
	
	room_type = models.CharField(max_length=20 , choices=TYPE_CHOICES, default="non-ac")
	roomno = models.CharField(max_length=5)
	fully_allocated = models.BooleanField(default=False)

	class Meta:
		ordering = ['room_type','roomno']
	

	def __str__(self):
		return self.roomno

	def get_absolute_url(self):
		return reverse('room:detail', kwargs={'id':self.id}) 

class Bed(models.Model):

	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	allocated_count = models.IntegerField(default=0)
	A = models.BooleanField(default=False)
	a_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	B = models.BooleanField(default=False)
	b_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	C = models.BooleanField(default=False)
	c_allocated_to = models.CharField(max_length=10, null=True, blank=True)
	D = models.BooleanField(default=False)
	d_allocated_to = models.CharField(max_length=10, null=True, blank=True)
