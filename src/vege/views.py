from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description, 
        )

        return redirect( 'receipes/')

    receipe_data = Receipe.objects.all()

    if request.GET.get('search'):
        receipe_data = receipe_data.filter(receipe_name__icontains = request.GET.get('search') )

    data = {
        'receipe_data' : receipe_data
    }
    return render(request, 'receipes.html', data)

@login_required(login_url="/login/")
def delete_receipe(request, id):
    receipe_Data = Receipe.objects.get(id = id)
    receipe_Data.delete()
    return redirect( 'receipes/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    receipe_dat = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        
        receipe_dat.receipe_name = receipe_name
        receipe_dat.receipe_description = receipe_description 

        if receipe_image:
            receipe_dat.receipe_image = receipe_image
        

        receipe_dat.save()

        return redirect( 'receipes/')
    data = {'receipe_dat' : receipe_dat}
    print(receipe_dat.receipe_name)

    return render(request, 'receipes_update.html',data)

def login_page(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login (request, user)
            return redirect('/receipes/')
    
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST' :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username Already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account successfuly Created")
        return redirect('/register/')

    return render(request, 'register.html')