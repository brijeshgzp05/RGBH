from django import forms
from room.models import Room
from .models import Student


GENDER_CHOICES = [('Male','Male'), ('Female','Female')]
YEAR_CHOICES = [
	(1,'First'), 
	(2,'Second'),
	(3,'Third'),
	(4,'Fourth'),
	]

BRANCH_CHOICES = [
	('Computer Science and Engineering','Computer Science and Engineering'),
	('Electronics and Communication Engineering','Electronics and Communication Engineering'),
	('Mechanical Engineering','Mechanical Engineering'),
	('Aeronautical Engineering','Aeronautical Engineering'),
	]
class StudentForm(forms.Form):
	name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control', 'placeholder':'Name', "required":"required"}))
	rollno = forms.CharField(required=False,label="Roll No.", widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Roll No.'}))
	branch = forms.CharField(label='Branch', widget=forms.Select(choices=BRANCH_CHOICES, attrs={'class':'form-control', "required":"required"}))
	dob = forms.DateField(label="Date of birth", widget=forms.SelectDateWidget(years=range(1990, 2010), attrs={'class':'form-control'}))#(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Date of Birth'}))
	
	gender = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_CHOICES, attrs={'class':'form-control', "required":"required"}))
	aadhar = forms.CharField(required=False,label="Aadhar No.", widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Aadhar No'}))
	mobile = forms.CharField(label="Mobile No.", widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Mobile No',"required":"required"}))
	fees_paid = forms.IntegerField(label="Fees paid", widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Fees paid',"required":"required"}))
	address = forms.CharField(label="Address",widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Address',"required":"required"}))
	email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Email'}))
	year = forms.CharField(label='Year', widget=forms.Select(choices=YEAR_CHOICES, attrs={'class':'form-control'}))
	roomno = forms.CharField(label='Room No.', widget=forms.TextInput(attrs={'class':'form-control',"required":"required"}))
	


	def clean_mobile(self):

		mobile = self.cleaned_data.get("mobile")
		try:
			a = int(mobile)
		except:
			raise forms.ValidationError("Incorrect mobile number")
		if len(mobile)!=10:
			raise forms.ValidationError("Incorrect mobile number")

		return mobile


	def clean_rollno(self):
		rollno = self.cleaned_data.get("rollno")
		
		if len(rollno)>10:
			raise forms.ValidationError("Incorrect roll number")
		return rollno

	def clean_aadhar(self):

		aadhar = self.cleaned_data.get("aadhar")

		l = len(aadhar)

		if l>0 and l!=12:
			raise forms.ValidationError("Incorrect Aadhar number")

		return aadhar

