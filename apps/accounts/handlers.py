import jwt
import os
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from rest_framework.views import APIView
from . import models, serializers
from .face_recognizer import recognize_user


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        face_biometerics = request.FILES.get("faceBiometeric")
        user = recognize_user(face_biometerics)
        if user:
            # Complete the login flow
            response = super().post(request, *args, **kwargs)
            access_token = response.data.get("access")
            decoded_token = jwt.decode(
                access_token,
                key=os.environ.get("SECRET_KEY"),
                algorithms=[
                    "HS256",
                ],
            )
            user_id = decoded_token.get("user_id")
            if user.id == user_id:
                return response

        return Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data={"message": "User facial biometeric error"},
        )
        # Customize the behavior here
        #
        # Modify the response here if needed
        #


@api_view(["GET"])
def allowed_views_handler(request):
    allowed_views = models.AllowedView.objects.all().order_by("-created_at")
    allowed_views_serializer = serializers.AllowedViewSerializer(
        allowed_views, many=True
    )
    return Response(status=status.HTTP_200_OK, data=allowed_views_serializer.data)


@api_view(["POST"])
def logout_handler(request):
    refresh_token = request.data.get("refresh_token")
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response(status=status.HTTP_205_RESET_CONTENT)


@api_view(["GET"])
def user_details_handler(request):
    logged_in_user = request.user
    user_serializer = serializers.UserSerializer(logged_in_user, many=False)

    return Response(status=status.HTTP_200_OK, data=user_serializer.data)
