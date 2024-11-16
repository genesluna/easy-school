from typing import Any, Dict
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from src.exceptions import RepositoryError
from src.product.forms import ProductForm
from src.product.models import Product
from src.product.repository import ProductRepository


class ListProductsView(ListView):
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        repository = ProductRepository()
        page = self.request.GET.get("page", 1)
        search_query = self.request.GET.get("search")
        order_by = self.request.GET.get("order_by")

        return repository.list(search_query=search_query, order_by=order_by, page=int(page), per_page=self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        repository = ProductRepository()
        search_query = self.request.GET.get("search")

        context.update(
            {
                "total_products": repository.count(search_query=search_query),
                "search_query": search_query,
                "current_order": self.request.GET.get("order_by", ""),
            }
        )
        return context


class CreateStudentView(SuccessMessageMixin, CreateView):

    template_name = "product/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list_products")
    success_message = "Product was created successfully"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Criar Produto"
        context["action"] = "Create"
        return context

    def form_valid(self, form):
        try:
            repository = ProductRepository()
            self.object = repository.create(**form.cleaned_data)
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(self.get_success_url())
        except RepositoryError as e:
            messages.error(self.request, str(e))
            return super().form_invalid(form)
