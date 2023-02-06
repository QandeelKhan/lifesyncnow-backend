# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from rest_framework import authentication, permissions, status, viewsets
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import User

# class UserViewSet(viewsets.ModelViewSet):
#     authentication_classes = [authentication.TokenAuthentication,]
#     permission_classes = [permissions.IsAuthenticated,]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @action(methods=['get'], detail=False)
#     def me(self, request, *args, **kwargs):
#         user = request.user
#         return Response({
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#         })

#     @action(methods=['post'], detail=False)
#     def logout(self, request, *args, **kwargs):
#         request.user.auth_token.delete()
#         return Response({'detail': 'Successfully logged out.'})

# class LoginView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# class SignupView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         if not username or not password or not email:
#             return Response({'error': 'Please provide all the required fields'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             User.objects.g


from rest_framework.response import Response
from rest_framework.views import APIView, status
from django.contrib.auth import authenticate
from UserManagement.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from UserManagement.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Generate token manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        # serializer can return 2 objects. 1 serializer.data gives us data, 2 serializer.errors gives us "errors" from serializer if happened so we can access and manage error styles in frontend as well if we want


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_token_for_user(user)
            return Response({'token': token, 'msg': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {"non_field_errors": ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        # because we 'raise_exception=True' (which is by default false),so we don't really need this if statement because this is used only when want to use our custom exception msgs or status codes(by default 400-bad-request) and in that scenarios we don't set the 'raise_exception=True'.
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
