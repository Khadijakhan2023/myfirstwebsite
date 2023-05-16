from django.shortcuts import render
from.import views
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'page/home.html')

def about(requst):
    return render(requst,'page/about.html')

def contact(requst):
    if requst.method=='post':
        v_name=requst.POST.get('firstname')
        v_email=requst.POST.get('email')
        v_message=requst.POST.get('Massege')
        v_subject=requst.POST.get('Subject')
        v_contact=Contact(name=v_name,email=v_email,subject=v_subject,message=v_message)
        v_contact.save()
        return render(requst,'page/thank.html')
    else:
        return render(requst,'page/contact.html')