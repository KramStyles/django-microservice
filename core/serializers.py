from rest_framework import serializers

from core.models import Project, User


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer."""

    class Meta:
        """Meta class for Product Serializer."""
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    class Meta:
        """Meta class for User Serializer."""
        model = User
        fields = "__all__"
