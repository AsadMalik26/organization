from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skill.models import Skill
from skill.serializers import SkillSerializer


# Create your views here.
class SkillsAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id:
            skill = Skill.objects.get(id=id)
            serializer = SkillSerializer(skill)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            skills = Skill.objects.all()
            serializer = SkillSerializer(skills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill = Skill.objects.get(id=request.data.get('id'))
        serializer.update(skill, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        skill = Skill.objects.get(id=request.query_params.get('id'))
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
