from django.urls import path

from src.course.views import ListCoursesView


urlpatterns = [
    path("", ListCoursesView.as_view(), name="list_courses"),
]
