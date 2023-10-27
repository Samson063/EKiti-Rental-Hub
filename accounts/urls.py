from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "accounts"

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('<username>/', views.get_profile, name='profile'),
    # path('settings', views.settings, name='settings'),
]