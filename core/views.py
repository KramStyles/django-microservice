import random

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.models import Project, User
from core.producer import publish
from core.serializers import ProductSerializer, UserSerializer


class ProjectViewSet(ModelViewSet):
    """Project ViewSet."""
    serializer_class = ProductSerializer
    queryset = Project.objects.all()

    def list(self, request, *args, **kwargs):
        publish()
        return super().list(request, *args, **kwargs)


class UserViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    """User API View."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, url_path="random-user")
    def random_user(self, request):
        if self.queryset:
            user = random.choice(self.queryset)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        return Response(self.queryset)
