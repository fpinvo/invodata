from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.permissions import get_permission_class
from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        get_permission_class(
            {
                "POST": "add_user",
                "PUT": "change_user",
                "PATCH": "change_user",
                "DELETE": "delete_user",
            }
        ),
    ]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
