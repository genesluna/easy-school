from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from src.api.serializers import CourseSerializer, ProductSerializer, StudentSerializer
from src.course.repository import CourseRepository
from src.product.repository import ProductRepository
from src.student.repository import StudentRepository


class StudentAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        repository = StudentRepository()
        students = repository.list()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class CourseAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        repository = CourseRepository()
        courses = repository.list()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        repository = ProductRepository()
        products = repository.list()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
