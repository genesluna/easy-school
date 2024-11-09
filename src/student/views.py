from django.views.generic import ListView
from src.student.repository import StudentRepository


class ListStudentsView(ListView):
    template_name = "student/list.html"
    context_object_name = "students"
    paginate_by = 10

    def get_queryset(self):
        repository = StudentRepository()
        page = self.request.GET.get("page", 1)
        search_query = self.request.GET.get("search")
        order_by = self.request.GET.get("order_by")

        return repository.list(search_query=search_query, order_by=order_by, page=int(page), per_page=self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        repository = StudentRepository()
        search_query = self.request.GET.get("search")

        context.update(
            {
                "total_students": repository.count(search_query=search_query),
                "search_query": search_query,
                "current_order": self.request.GET.get("order_by", ""),
            }
        )
        return context
