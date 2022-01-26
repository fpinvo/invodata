from django.contrib.auth.models import Permission
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer
from django.db.models import Q

from common.models import Role, Project, ProjectUser, ProviderCategory, Provider
from common.permissions import get_permission_class
from common.serializers import PermissionSerializer, RoleSerializer, RoleCreateSerializer, ProjectSerializer, \
    ProjectUserSerializer, ProjectUserListSerializer, ProviderCategorySerializer, ProviderSerializer


class PermissionViewSet(ModelViewSet):
    permission_classes = [

    ]
    serializer_class = PermissionSerializer
    renderer_classes = (JSONRenderer,)
    queryset = Permission.objects.filter(
        content_type__model__in=[
            'user',
            'role',
            'project',
            'projectuser'
        ]
    )
    pagination_class = None
    http_method_names = ["get"]


class RoleViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]
    renderer_classes = (JSONRenderer,)
    queryset = Role.objects.filter()

    def get_serializer_class(self):
        action_serializer_mapping = {
            'list': RoleSerializer,
            'retrieve': RoleSerializer,
            'create': RoleCreateSerializer,
            'update': RoleCreateSerializer,
            'partial_update': RoleCreateSerializer,
        }

        if self.action in action_serializer_mapping:
            return action_serializer_mapping[self.action]

        return Serializer


class ProjectViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        get_permission_class(
            {
                "POST": "add_project",
                "PUT": "change_project",
                "PATCH": "change_project",
                "DELETE": "delete_project",
            }
        ),
    ]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(Q(users__id__in=[self.request.user.id]) | Q(creator=self.request.user)).distinct()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['creator'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectUsersViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        get_permission_class(
            {
                "POST": "add_projectuser",
                "PUT": "change_projectuser",
                "PATCH": "change_projectuser",
                "DELETE": "delete_projectuser",
            }
        ),
    ]
    http_method_names = ["get"]

    def get_serializer_class(self):
        action_serializer_mapping = {
            'list': ProjectUserListSerializer,
            'retrieve': ProjectUserSerializer,
            'create': ProjectUserSerializer,
            'update': ProjectUserSerializer,
            'partial_update': ProjectUserSerializer,
        }

        if self.action in action_serializer_mapping:
            return action_serializer_mapping[self.action]

        return Serializer

    def get_queryset(self):
        return ProjectUser.objects.all()


class ProviderCategoryViewSet(ModelViewSet):
    serializer_class = ProviderCategorySerializer
    queryset = ProviderCategory.objects.all()


class ProviderViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def get_permissions(self):
        """Permissions override"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()
