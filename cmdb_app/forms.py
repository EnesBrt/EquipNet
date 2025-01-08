from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NetworkEquipment


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]

        if commit:
            user.save()
        return user


class AddEquipmentForm(forms.ModelForm):

    class Meta:
        model = NetworkEquipment
        fields = [
            "device_name",
            "device_type",
            "ip_address",
            "host",
            "username",
            "password",
            "location",
            "port",
        ]

    def save(self, commit=True):
        equipment = super().save(commit=False)

        if commit:
            equipment.save()
        return equipment
