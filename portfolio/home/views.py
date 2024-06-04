from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    #When we put path of urls in project ('') then we have to put / int the in search bar
    #return HttpResponse("This is my Homepage.")
    
    context = {'name':'Pratik','lastname':'Devkota'}
    return render(request,"home.html",context)




def about(request):
    #no need to put /  in path 
    #return HttpResponse("This is my Aboutpage. ")
    return render(request,"about.html")
 
 
def contact(request):
    # return HttpResponse("This is my Contactpage ")
    if request.method == "POST":
       # print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        #print(name,email,phone,password)
        ins = Contact(name=name,email=email,phone=phone,password=password)
        ins.save()
        print("The data has beeen returned to the db")
        
    return render(request,"contact.html")

def projects(request):
    
    #return HttpResponse("This is my Projectspage ")
    return render(request,"projects.html")