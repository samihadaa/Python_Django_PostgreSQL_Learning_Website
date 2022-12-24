from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects.all()
    context= {
        'courses':courses,
    }
    return render(request, 'courses/index.html',context)

def detail(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    context = {
        'course':course,
    }
    return render(request, 'courses/detail.html',context)