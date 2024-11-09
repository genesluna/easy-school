from typing import List, Optional
from django.db.models import Q
from src.student.models import Student


class StudentRepository:
    def __init__(self, student: Student = Student) -> None:
        self.student = student

    def list(
        self,
        search_query: Optional[str] = None,
        order_by: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> List[Student]:

        queryset = self.student.objects.all()

        # Search
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(lastname__icontains=search_query) | Q(email__icontains=search_query)
            )

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
        """Get total count of students, optionally filtered by search"""
        queryset = self.student.objects.all()

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(lastname__icontains=search_query) | Q(email__icontains=search_query)
            )

        return queryset.count()
