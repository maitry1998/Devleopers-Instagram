from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import ProjectSerializer
from projects.models import Project, Tag
from users.models import Profile

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {"GET": '/api/projects'},
        {"GET": '/api/projects/id'},
        {"POST": '/api/projects/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProjectid(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project = Project.objects.get(id=pk)
    user= request.user.profile
    data = request.data
    print("Data:", data)
    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)