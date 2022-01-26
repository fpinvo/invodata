from django.contrib.auth.models import Permission
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from common.models import Role, Project, ProjectUser, ProviderCategory, Provider
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


class ProviderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategory
        fields = [
            'id',
            'name',
        ]


class ProviderSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Provider
        extra_kwargs = {
            'category': {'write_only': True}
        }
        fields = [
            'id',
            'name',
            'category',
            'category_name',
            'connection_type',
            'default_ado_net_provider',
            'integration_type',
            'is_dialect',
            'is_dialect_over_ado_net',
            'is_dialect_over_odbc',
            'logo_url',
            'real_provider',
        ]
