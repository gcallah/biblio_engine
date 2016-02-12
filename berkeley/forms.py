from django import forms

from .models import PERSON_NAME_LEN, SUBJECT_CHOICES, Keyword


class SearchForm(forms.Form):
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    fname = forms.CharField(label='Author first name:',
            max_length=PERSON_NAME_LEN)
    year_after = forms.IntegerField(label='Published after (year):')
    year_before = forms.IntegerField(label='Published before (year):')
    subject = forms.ChoiceField(label='Subject', choices=SUBJECT_CHOICES)

    keyword = forms.ModelChoiceField(label='Keyword',
            queryset=Keyword.objects.all())
