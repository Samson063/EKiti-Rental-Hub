from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import SignupCode, EmailChangeCode, PasswordResetCode
from .models import send_multi_format_email
from .serializers import SignupSerializer, LoginSerializer
from .serializers import PasswordResetSerializer
from .serializers import PasswordResetVerifiedSerializer
from .serializers import EmailChangeSerializer
from .serializers import PasswordChangeSerializer
from .serializers import UserSerializer
from django.conf import settings
from .models import User, send_multi_format_email
from core.utils import *
from .serializers import *

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''View for handling user registration.

    This view handles user registration and  returns a response with the serialized data of the newly created user.
    '''
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']

            must_validate_email = getattr(settings, "AUTH_EMAIL_VERIFICATION", True)

            try:
                user = User.objects.get(email=email)
                if user.is_verified:
                    content = {'detail': _('Email address already taken.')}
                    return response(content, 400)

                try:
                    # Delete old signup codes
                    signup_code = SignupCode.objects.get(user=user)
                    signup_code.delete()
                except SignupCode.DoesNotExist:
                    pass

            except User.DoesNotExist:
                user = User.objects.create_user(email=email)

            # Set user fields provided
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            if not must_validate_email:
                user.is_verified = True
                send_multi_format_email('welcome_email',{'email': user.email, },target_email=user.email)
            user.save()

            if must_validate_email:
                # Create and associate signup code
                client_ip = get_client_ip(request)[0]
                if client_ip is None:
                    client_ip = '0.0.0.0'    # Unable to get the client's IP address
                signup_code = SignupCode.objects.create_signup_code(user, client_ip)
                signup_code.send_signup_email()

            content = {'email': email, 'first_name': first_name,
                       'last_name': last_name}
            return response(content, 201)

        return abort(400, serializer.errors)

class LoginView(TokenObtainPairView):
    '''View for handling user authentication.

    This view is responsible for authenticating a user using the provided email and password.
    
    Returns a response with the user's authentication token. 
    
    If the credentials are invalid, returns a 400 Bad Request response with an error message indicating that the provided credentials are incorrect.
    '''
    serializer_class = LoginSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    if request.method == 'POST':
        try:
            obj = User.objects.get(username=username)
            serializer = UserSerializer(obj)
            return response(serializer.data)
        except User.DoesNotExist:
            return abort(404)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return reponse(200, 'Logout successful!')