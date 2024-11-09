import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        db_table = "student"

    def __str__(self):
        return f"{self.name} {self.lastname}"
