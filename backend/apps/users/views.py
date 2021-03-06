from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import UserProfile

from .serializers import UserSerializer, UserProfileSerializer

from . import services


class UserRegisterView(APIView):
    permission_classes = []
    authentication_classes = []

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        user_type = serializers.CharField()
        email = serializers.EmailField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        address = serializers.CharField()
        latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
        longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
        password = serializers.CharField()
        buyer_type = serializers.CharField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = services.create_user(**serializer.validated_data)
        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserProfileUpdateView(APIView):
    class InputSerializer(serializers.Serializer):
        full_name = serializers.CharField(required=False, allow_blank=True)
        phone_number = serializers.CharField(required=False, allow_blank=True)
        email = serializers.EmailField(required=False, allow_blank=True)
        address = serializers.CharField(required=False, allow_blank=True)
        longitude = serializers.DecimalField(
            max_digits=9, decimal_places=6, required=False, allow_null=True
        )
        latitude = serializers.DecimalField(
            max_digits=9, decimal_places=6, required=False, allow_null=True
        )

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = services.update_user(user=request.user, **serializer.validated_data)
        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserProfileDetailView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class SellerListView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        profiles = UserProfile.objects.filter(user_type='seller')
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = UserProfile.objects.filter(user_type="seller")
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserDeleteView(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(
                username=serializer.validated_data["username"]
            )
        except User.DoesNotExist:
            user = None

        if user is None:
            return Response("Couldn't delete the user.")

        user.delete()
        return Response("User was deleted successfully.")
