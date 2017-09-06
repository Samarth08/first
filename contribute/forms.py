from django import forms
from .models import SignUp
from django.core.exceptions import ImproperlyConfigured
class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        exclude=[]
    def clean_title(self):
        title = self.cleaned_data.get('title')
       #       if not extension =="edu":
        #    raise forms.ValidationError("Please use a valid .EDU mail address")
        return title
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if "fcuk" in body:
         raise forms.ValidationError("You used an inapproriate word")
        return body
