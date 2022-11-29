from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable' : "tkushal is greatt",
        'variable1' : "rohan is great"
        
    }
    return render(request,"index.html", context)
    #return HttpResponse("this is homepage1")

def about(request):
     return render(request,"about.html")
     #return HttpResponse("this is about page")

def services(request):
     return render(request,"services.html")
    #return HttpResponse("this is service page")

def contact(request):   
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc,date= datetime.today())
        contact.save()
    return render(request,"contact.html")
    #return HttpResponse("this is conatact page")

def ice(request):
    return render(request, "ice.html")
    

def vanilla(request):
     return render(request,"vanilla.html")
 
 
def req(request):
     return render(request,"req.html")
 
def checkout(request):
    return render(request,"checkout.html")
