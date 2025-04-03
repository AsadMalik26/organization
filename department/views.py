from logging import exception

from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from department.models import Department
from department.serializers import DepartmentSerializer


# Create your views here.
class DepartmentListAPIView(APIView):
    def get(self, request, format=None):
        queryset = Department.objects.all()
        print(queryset, 'get')
        return Response(DepartmentSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class DepartmentGetAPIView(APIView):
    def get(self, request, format=None, pk=None):
        # search for pk method
        if not request.query_params.get('id'):
            raise exceptions.APIException()
        queryset = Department.objects.get(id=request.query_params.get('id'))
        return Response(DepartmentSerializer(queryset).data, status=status.HTTP_200_OK)


class DepartmentListArnonAPIView(APIView):
    queryset = Department.objects.all()

    def get(self, request, *args, **kwargs):
        print(self.queryset, 'get')
        return Response(DepartmentSerializer(self.queryset, many=True).data, status=status.HTTP_200_OK)


""" 
there are three types of creation method.
1. Simple Plane
2. Model method
3. Serializer method
"""


# 1. Simple Plane
class DepartmentCreateAPIView(APIView):
    def post(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        department = Department.objects.create(
            name=serialized_data.data.get('name'),
        )

        return Response(DepartmentSerializer(department).data, status=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        department = Department.objects.get(id=request.data.get('id'))
        department.name = serialized_data.data.get('name')
        department.save()
        return Response(DepartmentSerializer(department).data, status=status.HTTP_200_OK)


# 2. Model method
class DepartmentCreateWithModelView(APIView):
    def post(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        department = Department.objects.create(**serialized_data.validated_data)

        return Response(DepartmentSerializer(department).data, status=status.HTTP_201_CREATED)

    # def put(self, request, format=None):
    #     serialized_data = DepartmentSerializer(data=request.data)
    #     serialized_data.is_valid(raise_exception=True)
    #     department = Department.objects.get(id=request.data.get('id'))
    #     # it raise exception on below line for unique constriants
    #     Department.objects.update(**serialized_data)
    #
    #     return Response(DepartmentSerializer(department).data, status=status.HTTP_200_OK)

# 3. Serializer method
class DepartmentCreateWithSerializerView(APIView):
    def post(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        department = serialized_data.save()

        return Response(DepartmentSerializer(department).data, status=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        department = Department.objects.get(id=request.data.get('id'))
        serialized_data.update(department, serialized_data.validated_data)

        return Response(DepartmentSerializer(department).data, status=status.HTTP_200_OK)


class DepartmentUpdateAPIView(APIView):
    def put(self, request, format=None):
        serialized_data = DepartmentSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        department = Department.objects.get(id=request.data.get('id'))
        department.name = serialized_data.data.get('name')
        department.save()
        return Response(DepartmentSerializer(department).data, status=status.HTTP_200_OK)

class DepartmentDeleteAPIView(APIView):
    def delete(self, request, format=None):
        department = Department.objects.get(id=request.query_params.get('id'))
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)