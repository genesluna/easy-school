from typing import List, Optional
from django.db.models import Q
from src.exceptions import RepositoryError
from src.product.models import Product


class ProductRepository:
    def __init__(self, product: Product = Product) -> None:
        self.product = product

    def list(
        self,
        search_query: Optional[str] = None,
        order_by: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> List[Product]:

        queryset = self.product.objects.all()

        # Search
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))

        # Ordering
        if order_by:
            if order_by.startswith("-"):
                order_by = order_by[1:]
                queryset = queryset.order_by(f"-{order_by}")
            else:
                queryset = queryset.order_by(order_by)

        # Pagination
        if page is not None and per_page is not None:
            start = (page - 1) * per_page
            end = start + per_page
            queryset = queryset[start:end]

        return list(queryset)

    def count(self, search_query: Optional[str] = None) -> int:
        """Get total count of products, optionally filtered by search"""
        queryset = self.product.objects.all()

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))

        return queryset.count()

    def create(self, **data) -> Product | RepositoryError:
        try:
            product = Product.objects.create(**data)
            return product
        except Exception as e:
            raise RepositoryError(f"Failed to create product: {str(e)}")
