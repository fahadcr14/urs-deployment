from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

#First we have to i,port the model we want to use
from .models import User_Data
import os
#
import openpyxl
from django.shortcuts import render
from .models import University

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))






# Create your views here.
def index(request):
    return render(request, 'index.html')

def newaccountform(request):
    #Below code is to get the inputs that are in register.html
    #This data will be saved in the database in users
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['newpassword']
        if password == password2:
            #Below if will check if an email already exists or not
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('newaccountform')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('newaccountform')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                data_user = User_Data(username= username, email= email, password= password, confirm_password= password2)
                user.save()
                data_user.save()
                return redirect('form')
        
        else:
            messages.info(request, 'Password not the same')
            return redirect('newaccountform')
    else:
        return render(request, 'newaccountform.html')

def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)

        #To check if user is actually a user of platform
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('form')
        
    else:
        return render(request, 'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request, 'about.html')

#injection 
def uploadd():
    
    file = 'C:\\Users\\cr7\\Downloads\\World QS Ranking.xlsx'
    print(file)  # check if the file path is correct




    wb = openpyxl.load_workbook(file)
    ws = wb.active

    for row in ws.iter_rows(min_row=2):
        name = row[0].value
        impact_rank = row[1].value
        openness_rank = row[2].value
        global_rank = row[3].value

        University.objects.create(name=name, impact_rank=impact_rank, openness_rank=openness_rank, global_rank=global_rank)

        #messages.success(request, "Data uploaded successfully!")
    print(f'succesfully added the data')


def getyourdestination(request):
    
    universities = University.objects.all()
    if request.method == 'POST':
        university_name = request.POST['university']
        university = University.objects.get(name=university_name)
        return render(request, 'getyourdestination.html', {'universities': universities, 'university': university})
    else:
        return render(request, 'getyourdestination.html', {'universities': universities})

def contact(request):
    return render(request, 'contact.html')

def post(request, pk):
    return render(request, 'post.html', {'pk' : pk})

    
