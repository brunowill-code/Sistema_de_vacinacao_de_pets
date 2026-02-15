from rest_framework import generics, permissions
from ..serializers.register_serializer import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT
            )

        except Exception:
            return Response(
                {"error": "Token inválido ou expirado."},
                status=status.HTTP_400_BAD_REQUEST
            )
    