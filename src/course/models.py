import uuid
from django.db import models
from src.student.models import Student


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    students = models.ManyToManyField(Student, related_name="courses", verbose_name="Alunos")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = "course"

    def __str__(self):
        return self.title
