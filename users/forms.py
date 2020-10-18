from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Category

class UserRegisterForm(UserCreationForm):
   
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    email = forms.EmailField()
    age=forms.IntegerField()
    occupation=forms.CharField()
    qualification=forms.CharField(widget=forms.Textarea)
    expertise=forms.CharField()
    Current_Projects=forms.CharField(widget=forms.Textarea)
    duration=forms.CharField()
    sponsorship=forms.CharField()
    Completed_project=forms.CharField(widget=forms.Textarea)
    Year_of_Completion=forms.CharField()

    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2','category','age', 'qualification','occupation','expertise','Current_Projects','duration','sponsorship','Completed_project','Year_of_Completion']


   


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['occupation','qualification','age','expertise','category','Current_Projects','Completed_project','sponsorship','Year_of_Completion','image']


