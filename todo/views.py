from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

from .models import todo




# Create your views here.
@login_required
def index(request):
    if  request.user.is_authenticated:
        user=request.user
        alltodo=todo.objects.filter(user=user)
        if request.method == 'POST':
        
            title=request.POST['title']
            desc=request.POST['desc']
        
            store=todo(title=title,desc=desc)
            store.user=user
            store.save()
            messages.success(request,"Your todo has been saved")
           
          
    
        
    return render(request,"index.html",{"todoes":alltodo})

def delete_task(request, pk):
    task = todo.objects.get(id=pk)
    task.delete()
    messages.success(request, 'Your Todo has been deleted.')
    return redirect("index")






def register(request):
    if request.method =="POST":

        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        Password=request.POST['Password']
        

        myuser=User.objects.create_user(username,email,first_name=fname,last_name=lname,password=Password)
        myuser.save()
        messages.success(request, 'Your account have been created successfully.')
        

        return redirect(index)
    
    
    return render(request,"register.html")



def login_page(request):
    if request.method == "POST":

        uname=request.POST['uname']
        password1=request.POST['password1']


        User=authenticate(username=uname,password=password1)

        if User is not None:
            login(request,User)
            messages.success(request, f'welcome: {uname}')
            return redirect(index)

        
        else:
            messages.error(request,'your username or password is invalid')
            return redirect(login_page)
            

    
    return render(request,"login.html")



def logout_page(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")


