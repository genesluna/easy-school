import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    expiration_date = models.DateField(verbose_name="Data de Validade")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        db_table = "product"

    def __str__(self):
        return f"{self.name}"
