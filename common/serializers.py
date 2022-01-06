from django.contrib.auth.models import Permission
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from common.models import Role, Project, ProjectUser
from users.serializers import UserSerializer


class PermissionSerializer(FlexFieldsModelSerializer):
    model_name = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = "__all__"

    def get_model_name(self, instance):
        return instance.content_type.name


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the project model"""

    class Meta:
        model = Project
        extra_kwargs = {
            'creator': {'write_only': True}
        }
        fields = [
            'id',
            'name',
            'creator',
        ]


class RoleSerializer(serializers.ModelSerializer):
    """Serializer for the Role model"""
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'permissions'
        ]


class RoleCreateSerializer(serializers.ModelSerializer):
    """Serializer for the Create Role model"""

    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'permissions'
        ]


class ProjectUserSerializer(serializers.ModelSerializer):
    """Serializer for the Project User model"""

    class Meta:
        model = ProjectUser
        fields = [
            'id',
            'project',
            'user',
            'role'
        ]


class ProjectUserListSerializer(serializers.ModelSerializer):
    """Serializer for the List of Project User model"""
    user = UserSerializer()

    class Meta:
        model = ProjectUser
        fields = [
            'id',
            'project',
            'user',
            'role'
        ]
