from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Employee
from employee.serializers import EmployeeSerializer


# Create your views here.

class EmployeeAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = Employee.objects.get(id=request.data.get('id'))
        serializer.update(employee, serializer.validated_data)
        return Response(EmployeeSerializer(employee).data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        employee = Employee.objects.get(id=request.query_params.get('id'))
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
