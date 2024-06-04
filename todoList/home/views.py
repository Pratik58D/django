from django.shortcuts import render, HttpResponse
from home.models import Tasks

# Create your views here.
def home(request):
    context = {
            "success": True
        }
    if request.method == "POST":
        #handle form
        taskTitle = request.POST.get('title')
        taskDesc = request.POST.get('desc')
        #print(title,desc)
        
        ins = Tasks(taskTitle=taskTitle,taskDesc =taskDesc)
        ins.save()
        
        
        
    return render(request,"index.html",context)


def about(request):
    return render (request,"about.html")