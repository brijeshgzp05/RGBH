from django.shortcuts import render
from .models import Staff
from django.contrib.auth.decorators import login_required

@login_required
def StaffListView(request):
	 staff = Staff.objects.all()
	 return render(request, 'staff/staff_list.html', {'staff':staff})
