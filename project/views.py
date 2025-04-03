from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Project
from project.serializers import ProjectSerializer


# Create your views here.

class ProjectAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            project = Project.objects.all()
            serializer = ProjectSerializer(project, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = Project.objects.get(id=request.data.get('id'))
        serializer.update(project, serializer.validated_data)
        return Response(ProjectSerializer(project).data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        project = Project.objects.get(id=request.query_params.get('id'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
