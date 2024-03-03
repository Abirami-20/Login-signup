from django import forms
from app1.models import Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model= Register
        fields='__all__'
        
