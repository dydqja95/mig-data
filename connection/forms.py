from django import forms
from .models import Connection

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['conn_name', 'conn_type', 'owner', 'ip', 'port', 'user', 'pwd', 'extra']  # 사용할 필드
