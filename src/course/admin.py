from django.contrib import admin

from src.course.models import Course


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course)
