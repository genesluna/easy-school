from django.contrib import admin

from src.student.models import Student


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student)
