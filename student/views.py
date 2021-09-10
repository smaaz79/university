from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *

# Create your views here.
def add_student(request):
    courses = Course.objects.all()
    return render(request, "/Users/mac/Desktop/project/3.2/university/student/templates/student/student.html", {'courses':courses})

def adding_student(request):
    print(request.POST)
    firstname = request.POST.get('fname')
    lastname = request.POST.get('lname')
    street= request.POST.get('street')
    city= request.POST.get('city')
    state = request.POST.get('state')
    course_id = request.POST.get('scourse')
    #print(firstname,lastname, street, city, state, scourse)
    selected_course = Course.objects.get(id=course_id)
    a = Address(street=street, city=city, state=state)
    a.save()
    c = Student(fname=firstname, lname=lastname, address=a, course=selected_course)
    c.save()
    return HttpResponse("Student Added")

def view_student(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    addresses = Address.objects.all()
    return render(request, "/Users/mac/Desktop/project/3.2/university/student/templates/student/view.html", {'courses':courses, 'students':students, 'teachers':teachers, 'addresses':addresses})