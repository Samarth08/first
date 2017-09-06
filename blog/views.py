from django.shortcuts import render
from django.http import HttpResponse

def up(request):
    return render(request,'blog/main.html')

def down(request) :
    return render(request,'blog/workout.html')     

def chk(request):
    return render(request,'blog/biceps.html')

def chest(request):
    return render(request,'blog/chest.html')

def abs(request):
    return render(request,'blog/abs.html')

def back(request):
    return render(request,'blog/back.html')

def triceps(request):
    return render(request,'blog/triceps.html')

def shoulder(request):
    return render(request,'blog/shoulder.html')

def legs(request):
    return render(request,'blog/legs.html')

#def thank(request):
   # return render(request,'contribute/thankyou.html')
