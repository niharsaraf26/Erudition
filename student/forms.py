from django import forms
from django.apps import apps
Detail = apps.get_model('home', 'Detail')


class Edit(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['image']



