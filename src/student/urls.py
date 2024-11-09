from django.urls import path

from src.student.views import ListStudentsView


urlpatterns = [
    path("", ListStudentsView.as_view(), name="list_students"),
]
