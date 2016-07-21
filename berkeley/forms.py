from django import forms
from django.db.models.functions import Lower

from .models import PERSON_NAME_LEN, TYPE_CHOICES, Keyword, Journal, Subject


class SearchForm(forms.Form):
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    fname = forms.CharField(label='Author first name:',
            max_length=PERSON_NAME_LEN)
    year_after = forms.IntegerField(label='Published after (year):')
    year_before = forms.IntegerField(label='Published before (year):')
    pub_type = forms.ChoiceField(label='Type', choices=TYPE_CHOICES)
    subject = forms.ModelChoiceField(label='Subject',
            queryset=Subject.objects.all().order_by('name'))
    journal = forms.ModelChoiceField(label='Journal',
            queryset=Journal.objects.all().order_by('name'))
    kwlist = Keyword.objects.all().order_by(Lower('name'))
    keyword1 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)
    keyword2 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)
