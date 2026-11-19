from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models.functions import Lower

from .models import PERSON_NAME_LEN, Keyword, Subject, pub_type_choices


class SearchForm(forms.Form):
    forms.Form.use_required_attribute = False
    lname = forms.CharField(label='Author last name:',
            max_length=PERSON_NAME_LEN)
    #fname = forms.CharField(label='Author first name:',
       #     max_length=PERSON_NAME_LEN)
    reviewed = forms.CharField(label='Reviewed author last name:',
            max_length=PERSON_NAME_LEN)
    pub_type = forms.ChoiceField(label='Type', choices=pub_type_choices)
    start_year = forms.IntegerField(label='From year:')
    end_year = forms.IntegerField(label='To year:')
    subject = forms.ModelChoiceField(label='Category',
            queryset=Subject.objects.all().order_by('name'))
    #journal = forms.ModelChoiceField(label='Journal',
            #queryset=Journal.objects.all().order_by('name'))
    kwlist = Keyword.objects.all().order_by(Lower('name'))
    keyword1 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)
    #keyword2 = forms.ModelChoiceField(label='Keyword', queryset=kwlist)


class EditorLoginForm(AuthenticationForm):
    """The login form: only editors (staff accounts) may log in. Other
    accounts would be turned away by the admin pages anyway, so they are
    told why here instead."""
    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "Your username and password did not match. "
                         "Please try again.",
        "not_editor": "This account is not set up as an editor yet. Ask "
                      "the site administrator to give it editor rights "
                      "(manage.py add_editor).",
    }

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise forms.ValidationError(self.error_messages["not_editor"],
                                        code="not_editor")
