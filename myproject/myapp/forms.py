from django import forms
from .models import MartialArtsStudent

class MartialArtsStudentForm(forms.ModelForm):
    class Meta:
        model = MartialArtsStudent
        fields = ['name', 'belt_color', 'age', 'discipline']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
