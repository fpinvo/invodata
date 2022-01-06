from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission


# from common.models import ProjectPermissions


def get_permission_class(permission_map):
    class GenericPermission(BasePermission):
        def has_permission(self, request, view):
            user = request.user
            required_permission = permission_map.get(request.method)
            if user.is_anonymous:
                return False
            if user.is_superuser:
                return True

            try:
                project_id = request.query_params.get('project_id')
                user_permissions = user.projects.filter(project__id=project_id).first().role.permissions
                if not user.is_authenticated:
                    return False
                if not required_permission:
                    return True
                if user_permissions.filter(codename=required_permission):
                    return True
            except Permission.DoesNotExist:
                return False

    return GenericPermission
