from django.contrib import admin

# Register your models here.

from contribute.models import SignUp
admin.site.register(SignUp)


#from .forms import SignUpForm


#class SignUpAdmin(admin.ModelAdmin):
 #   list_display =["__unicode__","timestamp","updated"]
  #  form=SignUpForm
