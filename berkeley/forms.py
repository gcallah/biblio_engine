from django import forms

from .models import PERSON_NAME_LEN, SUBJECT_CHOICES, Keyword, Journal


class SearchForm(forms.Form):
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    fname = forms.CharField(label='Author first name:',
            max_length=PERSON_NAME_LEN)
    year_after = forms.IntegerField(label='Published after (year):')
    year_before = forms.IntegerField(label='Published before (year):')
    subject = forms.ChoiceField(label='Subject', choices=SUBJECT_CHOICES)
    journal = forms.ModelChoiceField(label='Journal',
            queryset=Journal.objects.all().order_by('name'))
    keyword = forms.ModelChoiceField(label='Keyword',
            queryset=Keyword.objects.all().order_by('name'))
