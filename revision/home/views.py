from django.shortcuts import render , HttpResponse
from home.models import Contact

# Create your views here.
'''
def home(request):
    return HttpResponse("This is pratik.")

def contact(request):
    return HttpResponse("9858056222")

def name(request):
    return HttpResponse("ram, sam, hari, pratik  made this")

'''
def home(request):
    #return HttpResponse("this is my homepage")
    
    
    return render(request,"home.html")

def contact(request):
    if request.method == "POST":
        print("This has been posted")
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST ["phone"]
        message = request.POST["message"]
        #print(name,email,phone,message)
        
        #these line are used  return data at database
        contactInstance = Contact(name=name,email=email,phone=phone,message= message)
        contactInstance.save()
        print("this is saved in database")
    
    
    
    #return HttpResponse("This is Contact Page.")
    return render(request,"contact.html")

def projects(request):
    #return HttpResponse("This is project page.")
    return render(request,"projects.html")

def about(request):
    #return HttpResponse("This is about page")
    
    
    # passsing variable in about.html
    context = {'name': 'Pratik' , 'age': 22}
    
    
    return render(request,"about.html" , context)

