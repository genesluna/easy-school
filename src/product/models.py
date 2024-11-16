import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"

    def __str__(self):
        return f"{self.name}"
