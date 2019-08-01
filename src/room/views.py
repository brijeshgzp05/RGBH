from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from students.models import Student
from .forms import RoomForm
from .models import Room, Bed

@login_required
def RoomAddView(request):
	form = RoomForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			room_type = form.cleaned_data.get('room_type')
			roomno = form.cleaned_data.get('roomno')
			
			room = Room(
				room_type = room_type,
				roomno = roomno,
				fully_allocated=False,
				)
			room.save()

			Bed.objects.create(room=room)
			messages.success(request, 'Room SuccessFully Added')
			return HttpResponseRedirect(reverse('room:list'))

	context = {
		'form':form
	} 

	return render(request, 'room/room_add.html', context)

@login_required
def RoomListView(request):
	rooms = Room.objects.all()
	context = {
		'rooms':rooms
	}
	return render(request, 'room/room_list.html', context)

@login_required
def RoomDetailView(request, id=None):
	room_obj = get_object_or_404(Room, id=id)
	instance = get_object_or_404(Bed, room=room_obj)
	beda=None;bedb=None;bedc=None;bedd=None
	if instance.A:
		beda = get_object_or_404(Student, mobile=instance.a_allocated_to)
	if instance.B:
		bedb = get_object_or_404(Student, mobile=instance.b_allocated_to)
	if instance.C:
		bedc = get_object_or_404(Student, mobile=instance.c_allocated_to)
	if instance.D:
		bedd = get_object_or_404(Student, mobile=instance.d_allocated_to)
	context = {
		'room':room_obj,
		'beda':beda,
		'bedb':bedb,
		'bedc':bedc,
		'bedd':bedd,

	}
	return render(request, 'room/room_details.html', context)
