from django import forms

from .models import PERSON_NAME_LEN, YEAR_LEN, SUBJECT_CHOICES


class SearchForm(forms.Form):
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    fname = forms.CharField(label='Author first name:',
            max_length=PERSON_NAME_LEN)
    year = forms.CharField(label='Year:', max_length=YEAR_LEN)
    subject = forms.ChoiceField(label='Subject', choices=SUBJECT_CHOICES)
