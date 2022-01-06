"""URL patterns for the users app"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import PermissionViewSet, RoleViewSet, ProjectViewSet, ProjectUsersViewSet

router = DefaultRouter()

router.register('project', ProjectViewSet, '')
router.register('permission', PermissionViewSet, '')
router.register('project_users', ProjectUsersViewSet, '')
router.register('role', RoleViewSet, '')

urlpatterns = [
    path('', include(router.urls))
]
