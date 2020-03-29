from django import forms

from .models import UserGym


class UserForm(forms.ModelForm):
    class Meta:
        model = UserGym
        fields = ('fullname', 'cpf', 'rg', 'flag', 'card_number', 'card_name', 'medic_description', 'type_plan')