from django.urls import path

from .views import MyTokenObtainPairView, CustomUserCreation, LoginView, UserView, Logout

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', CustomUserCreation.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', Logout.as_view(), name='logout'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
