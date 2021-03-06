"""URL patterns for the users app"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, ObtainJSONWebToken

from .serializers import CustomJWTSerializer
from .views import UsersViewSet, UserSignupView

router = DefaultRouter()

router.register('', UsersViewSet, '')

urlpatterns = [
    path('login/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
    path('signup/', UserSignupView.as_view()),
    url(r'^password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include(router.urls))
]
