from django.contrib import admin

from .models import Student, Teacher

class StudentTagInline(admin.TabularInline):
    model = Student.teacher.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     inlines = [StudentTagInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentTagInline]