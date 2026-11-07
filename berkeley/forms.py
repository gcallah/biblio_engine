from django import forms
from django.db.models.functions import Lower

from .models import PERSON_NAME_LEN, TYPE_CHOICES, DEPT_LEN, Keyword, Journal, Subject, CATEGORIES


class SearchForm(forms.Form):
    forms.Form.use_required_attribute = False
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    #fname = forms.CharField(label='Author first name:',
       #     max_length=PERSON_NAME_LEN)
    reviewed = forms.CharField(label='Reviewed author last name:',
            max_length=PERSON_NAME_LEN)
    pub_type = forms.ChoiceField(label='Type', choices=TYPE_CHOICES)
    start_year = forms.IntegerField(label='From year:')
    end_year = forms.IntegerField(label='To year:')
    subject = forms.ModelChoiceField(label='Category',
            queryset=Subject.objects.all().order_by('name'))
    #journal = forms.ModelChoiceField(label='Journal',
            #queryset=Journal.objects.all().order_by('name'))
    kwlist = Keyword.objects.all().order_by(Lower('name'))
    keyword1 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)
    #keyword2 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)
