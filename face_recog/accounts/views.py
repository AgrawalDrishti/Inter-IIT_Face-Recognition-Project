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
    return render(request, 'dashboard.html', context )

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