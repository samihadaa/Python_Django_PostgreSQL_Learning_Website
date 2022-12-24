from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display=('summary','created_at')

admin.site.register(Course,CourseAdmin)