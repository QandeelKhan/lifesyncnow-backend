from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView, status, View
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from UserManagement.renderers import UserRenderer
from UserManagement.serializers import (
    SendPasswordResetEmailSerializer,
    UserChangePasswordSerializer,
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
    GoogleLoginSerializer
)


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    renderer_classes = [UserRenderer]

    def perform_create(self, serializer):
        user = serializer.save()
        token = get_token_for_user(user)
        self.headers.update({'Authorization': f"Bearer {token['access']}"})


# class UserRegistrationView(APIView):
#     renderer_classes = [UserRenderer]

#     def post(self, request, format=None):
#         serializer = UserRegistrationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token = get_token_for_user(user)
#         return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        # serializer can return 2 objects. 1 serializer.data gives us data, 2 serializer.errors gives us "errors" from serializer if happened so we can access and manage error styles in frontend as well if we want


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    # renderer_classes = [UserRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_token_for_user(user)
            self.headers.update({'Authorization': f"Bearer {token['access']}"})
            return Response({'token': token, 'msg': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {"non_field_errors": ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)


# class GoogleLoginAPIView(APIView):
#     permission_classes = []

#     def post(self, request):
#         serializer = GoogleLoginSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data
#             return Response({"token": user.auth_token.key})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password link sent Successfully. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully.'}, status=status.HTTP_200_OK)
