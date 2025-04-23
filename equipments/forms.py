from django import forms
from equipments.models import Equipments

class UpdateEquipmentsForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ['device_name', 'device_type', 'host']
        
        
class CreateEquipmentsForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ['device_name', 'device_type', 'host', 'username', 'password', 'port', 'secret']
        
        
        
        
