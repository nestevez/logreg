from django import forms

class Reg(forms.Form):
    fname = forms.CharField(label='First Name', max_length=50, min_length=2)
    lname = forms.CharField(label='Last Name', max_length=50, min_length=2)
    email = forms.EmailField(label='Email', max_length=100)
    pw = forms.CharField(label='Password', widget = forms.PasswordInput(), min_length=8)
    cpw = forms.CharField(label='Password Confirmation', widget = forms.PasswordInput())

class Log(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    pw = forms.CharField(label='Password', widget = forms.PasswordInput())
