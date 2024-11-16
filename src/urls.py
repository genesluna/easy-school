from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("src.student.urls")),
    path("courses/", include("src.course.urls")),
    path("products/", include("src.product.urls")),
]

admin.site.site_header = "🧑‍🏫 EasySchool"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Bem-vindo à EasySchool"
