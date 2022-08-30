from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Students
from django.urls import reverse

def index(request):
    mystudents = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {
     'mystudents': mystudents,
    }
    return HttpResponse(template.render(context, request))
    
def add_student_form(request):
    template = loader.get_template('student_form.html')
    return HttpResponse(template.render({}, request))

def save_student_form(request):
    student_first_name = request.POST['first_name']
    student_last_name = request.POST['last_name']
    student_age = request.POST['age']
    student_gender = request.POST['gender']
    student_address = request.POST['address']
    student_religion = request.POST['religion']
    student_contact = request.POST['contact']

    student = Students(
        first_name=student_first_name,
        last_name=student_last_name,
        age=student_age,
        gender=student_gender,
        address=student_address,
        religion=student_religion, 
        contact=student_contact)
    student.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    students = Students.objects.get(id=id)
    template = loader.get_template('student_update_form.html')
    context = {
        'students': students,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    student_first_name = request.POST['first_name']
    student_last_name = request.POST['last_name']
    student_age = request.POST['age']
    student_gender = request.POST['gender']
    student_address = request.POST['address']
    student_religion = request.POST['religion']
    student_contact = request.POST['contact']

    students = Students.objects.get(id=id)
    students.first_name = student_first_name
    students.last_name = student_last_name
    students.age = student_age
    students.gender = student_gender
    students.address = student_address
    students.religion = student_religion
    students.contact = student_contact
    students.save()

    return HttpResponseRedirect(reverse('index'))


