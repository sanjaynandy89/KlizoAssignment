from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print('user taken')
                messages.info(request,'user already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'Invalid user')
                return redirect('register')
            else:    
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('usercreated')
        
        else:
            print('password not matching')
            messages.info(request,'Password not same')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'Registration.html')
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
                auth.login(request,user)
                return redirect('/')
        else:    
                   messages.info(request,'Invalid user')
                   return redirect('login')
    else:
        return render(request,'Login.html')       
def logout(request):
    auth.logout(request)  
    return redirect('/') 