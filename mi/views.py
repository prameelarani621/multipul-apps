from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rahul(request):
    return render(request,'rahul.html')

def men(request):
    return HttpResponse('men will be men is a bad men')