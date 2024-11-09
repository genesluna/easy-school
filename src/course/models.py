import uuid
from django.db import models
from src.student.models import Student


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name="courses")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "course"

    def __str__(self):
        return self.title
