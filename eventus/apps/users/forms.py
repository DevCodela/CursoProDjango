from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario'
				}),
			'email' : forms.TextInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un email'
				}),
			'password' : forms.TextInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un password'
				})
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30, 
				widget = forms.TextInput(attrs = {
					'class' : 'form-control',
					'placeholder' : 'Ingresa un nombre de usuario'
					}))
	password = forms.CharField(max_length=30,
	 			widget = forms.TextInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa un password'
	 				}))