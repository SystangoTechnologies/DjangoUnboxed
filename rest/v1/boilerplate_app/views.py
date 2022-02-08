from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from boilerplate_app.models import Projects
from rest.v1.boilerplate_app.serializers import (ProjectsCreateSerializer, ProjectsListSerializer)


class ProjectAPIView(GenericAPIView):
    serializer_class = ProjectsListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        List all the projects.
        """
        try:
            projects = Projects.objects.all()
            project_serializer = ProjectsListSerializer(projects, many=True)

            projects = project_serializer.data
            return Response({'status': True,
                             'Response': projects},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        Create a project
        """
        try:
            data = request.data
            data['user'] = request.user.pk
            serializer = ProjectsCreateSerializer(data=data)
            if serializer.is_valid():
                project = serializer.create(serializer.data)
                return Response({'status': True,
                                 'project': project.id,
                                 'message': "Project Added Successfully"},
                                status=status.HTTP_200_OK)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
