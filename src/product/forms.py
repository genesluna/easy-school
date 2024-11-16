from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms
from src.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "expiration_date"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "required": "required"}),
            "description": forms.Textarea(attrs={"class": "form-control", "required": "required"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "required": "required"}),
            "expiration_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "required": "required"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 4:
            raise ValidationError("Name must be at least 4 characters long")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 10:
            raise ValidationError("Description must be at least 10 characters long")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Price must be greater than 0")
        return price

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data.get("expiration_date")
        if expiration_date:
            today = timezone.now().date()
            if expiration_date < today:
                raise ValidationError("Expiration date cannot be in the past")
        return expiration_date
