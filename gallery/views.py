from django.shortcuts import render
from.import views
# Create your views here.
def baby(request):
    return render(request,'gallery/baby.html')

def country(requst):
    return render(requst,'gallery/country.html')

def proudct(requst):
    return render(requst,'gallery/proudct.html')