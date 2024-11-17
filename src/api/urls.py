from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.api.views import CourseAPIView, ProductAPIView, StudentAPIView


urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("students/", StudentAPIView.as_view(), name="list_students"),
    path("courses/", CourseAPIView.as_view(), name="list_courses"),
    path("products/", ProductAPIView.as_view(), name="list_products"),
]

app_name = "api"
