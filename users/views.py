from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        # get_permission_class(
        #     {
        #         "POST": "add_user",
        #         "PUT": "change_user",
        #         "PATCH": "change_user",
        #         "DELETE": "delete_user",
        #     }
        # ),
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


class UserSignupView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.is_active = True
            user.save()
            return Response({"message": "User successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
