from django import forms
from .models import Item

class MenuUpdateForm(forms.ModelForm):
	day = forms.CharField(label="Day",widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control', 'placeholder':'Day'}))

	breakfast = forms.CharField(label='BreakFast', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BreakFast'}))

	lunch = forms.CharField(label='Lunck', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BreakFast'}))
	evening = forms.CharField(label='Evening', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lunch'}))
	dinner = forms.CharField(label='Dinner', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dinner'}))
	

	class Meta:
		model=Item
		fields=['day', 'breakfast', 'lunch', 'evening', 'dinner']