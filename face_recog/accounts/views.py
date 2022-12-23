import os
import face_recognition


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .models import *
from .forms import *
# from .decorators import allowed_users
# from .filters import OrderFilter 

def home(request):

    context = {}
    return render(request, 'homePage.html', context )

def teacherRegister(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            Teacher.objects.create(
                user=user
            )

            return redirect('teacherLogin')

    context = {'form':form}
    return render(request, 'teacher_register.html', context )

def studentRegister(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            Student.objects.create(
                user=user
            )

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password )

            login(request, user)

            return redirect('student_dashboard')

            # return redirect('teacherLogin')

    context = {'form':form}
    return render(request, 'student_register.html', context )

def teacherLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('dashboard')

    context = {}
    return render(request, 'teacher_login.html', context )

def studentLogin(request):

    context = {}
    return render(request, 'student_login.html', context )

def dashboard(request):

    context = {}
    # return render(request, 'dashboard.html', context )
    return redirect('http://localhost:2000/')

def student_dashboard(request):

    context = {}
    return render(request, 'student_dashboard.html', context )

def accountSettings(request):
    teacher = request.user.teacher
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'teacher_account_settings.html', context)

def StudentaccountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'account_settings.html', context)

# def loginPage(request):

#     context = {}
#     return render(request, 'login.html', context )

def uwu(request):
    
    with open('database.db') as f:
        data = f.read()


    x = data.split("$");

    y = data.split("%");

    #print(y[len(y)-2])
    #print(x[len(x)-2])

    latestimage = "tobeverified/" + x[len(x)-2]
    image = face_recognition.load_image_file(latestimage)
    encoding1 = face_recognition.face_encodings(image)[0]


    dir_path = 'static/images'

    count = 0
    const2 = -3;

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            print(path)
            image2 = face_recognition.load_image_file(f"static/images/{path}")
            
            if len(face_recognition.face_encodings(image2)) != 0:
                encoding2 = face_recognition.face_encodings(image2)[0]

                if (face_recognition.compare_faces([encoding1], encoding2) == [True]):
                    print("welcome", y[len(y)-2])
                    # return HttpResponse("Welcome")
                    const2 = 0;
                    context = {}
                    with open('database.db', 'w') as f:
                        pass
                    os.remove(f'{latestimage}')
                    return render(request, 'welcome.html', context )
                    
                    break

            
            


            #print(type(face_recognition.compare_faces([encoding1], encoding2)))
            
            else:
                continue


            

    if(const2 != 0):
        with open('database.db', 'w') as f:
            pass
        os.remove(f'{latestimage}')
        return HttpResponse('Not Verified')

    