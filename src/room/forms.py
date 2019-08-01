from django import forms
from .models import Room

TYPE_CHOICES = (
    ('ac','AC'),
    ('non-ac', 'NON-AC'),
    
)

class RoomForm(forms.ModelForm):
	room_type = forms.CharField(widget=forms.Select(choices=TYPE_CHOICES, attrs={'class':'form-control'}))
	roomno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Room No'}))
	class Meta:
		model = Room
		fields = ['room_type', 'roomno']



	def clean_roomno(self):
		roomno = self.cleaned_data.get("roomno")
		if len(Room.objects.filter(roomno=roomno)):
			raise forms.ValidationError("Room Already Exists")

		return roomno