from django import forms
from django.forms import forms, ModelForm

from admin123.models import Admins


class AdminsCreateForm(forms.Form):
    class Meta:
        model = Admins
        fields = ('login', 'password',)
        # fields.save()
