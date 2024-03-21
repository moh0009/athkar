from django import forms
from .models import User,Thkr

class User_Form_Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password","gender"]
        width ="w-100"
        widgets = {
           "first_name": forms.TextInput(attrs={"class":"form-control","placeholder":"mohamed"}),
           "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"muslim"}),
           "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"example@example.com"}),
           "username":forms.TextInput(attrs={"class":"form-control","placeholder":"moh7"}),
           "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
           "gender": forms.Select(attrs={"class":"form-select"}),
        }

class User_Form_Login(forms.Form):
    username = forms.CharField(label="Your Username :", max_length=150,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"moh7"}))
    password = forms.CharField(label="Your Password :",max_length=128,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))

class Form_Add(forms.ModelForm):
    class Meta:
        model = Thkr
        fields = ["thkr","repeat",]
        width ="w-100"
        widgets = {
           "thkr": forms.Textarea(attrs={"class":"form-control","placeholder":"thkr"}),
           "repeat":forms.NumberInput(attrs={"class":"form-control","placeholder":"Repeat times"}),
        }