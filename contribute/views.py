from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponse
def contribute(request):
    title = 'Welcome'
    form=SignUpForm(request.POST)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
    context={
        "title": title,
        "form":form
        }
    return render(request,"contribute/contribute.html",context)


