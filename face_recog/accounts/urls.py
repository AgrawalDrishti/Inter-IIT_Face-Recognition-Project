from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('uwu/', views.facerecog, name = "facerecog"),
    path('teacherRegister/', views.teacherRegister, name="teacherRegister"),
    path('studentRegister/', views.studentRegister, name="studentRegister"),
    path('teacherLogin/', views.teacherLogin, name="teacherLogin"),
    path('studentLogin/', views.studentLogin, name="studentLogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('student_dashboard/', views.student_dashboard, name="student_dashboard"),
    path('account/', views.accountSettings, name="account"),
    path('studentaccount/', views.StudentaccountSettings, name="studentaccount"),
    # path('dashboard/<str:pk>/', views.dashboard, name="dashboard"),
    # path('register/', views.registerPage, name="register"),
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('account/', views.accountSettings, name="account"),
]