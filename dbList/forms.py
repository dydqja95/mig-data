from django import forms
from .models import Connection

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['name', 'conn_type', 'host', 'port', 'login', 'password', 'extra']
        widgets = {
            'password': forms.PasswordInput(),
        }