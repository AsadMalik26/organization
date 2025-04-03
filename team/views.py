from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from team.models import Team
from team.serializers import TeamSerializer


# Create your views here.
class TeamsAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id:
            team = Team.objects.get(id=id)
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            skills = Team.objects.all()
            serializer = TeamSerializer(skills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        team = Team.objects.get(id=request.data.get('id'))
        serializer.update(team, serializer.validated_data)
        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        team = Team.objects.get(id=request.query_params.get('id'))
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
