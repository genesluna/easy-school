import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nome")
    lastname = models.CharField(max_length=100, verbose_name="Sobrenome")
    email = models.EmailField(unique=True, verbose_name="Email")

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = "student"

    def __str__(self):
        return f"{self.name} {self.lastname}"
