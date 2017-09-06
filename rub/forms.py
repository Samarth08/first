from django import forms
from .models import SignUp
from django.core.exceptions import ImproperlyConfigured
class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        exclude=[]
    def clean_title(self):
        title = self.cleaned_data.get('title')
        title_base,provider = title.split("@")
        domain,extension = provider.split('.')

        if not extension =="edu":
            raise forms.ValidationError("Please use a valid .EDU mail address")
        return title


    def clean_body(self):

        body = self.cleaned_data.get('body')
        return body
