from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import MenuUpdateForm
from .models import Item
# Create your views here.


def MenuListView(request):
	return render(request, 'menu/menu_list.html', {'menu':Item.objects.all()})


def MenuUpdateView(request, id=None):
	instance = get_object_or_404(Item, id=id)
	form = MenuUpdateForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Saved")
			return HttpResponseRedirect(reverse("menu:menu"))
	context = {
		'form':form,
		
	}
	return render(request, 'menu/menu_update.html', context)
