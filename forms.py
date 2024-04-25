from django import forms
from .models import Register, Login

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email','password']
class LoginForm(forms.Form):
    class Meta:
        model = Login
        fields = ['username','password']
   