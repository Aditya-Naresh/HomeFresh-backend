from django.shortcuts import render
from django.urls import path,include
from .views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    path('UserRegistrationView/',UserRegistrationView.as_view()),
    path('check_username/', CheckUsernameView.as_view(), name='check_username'),
    path('VerifyOTPView/',VerifyOTPView.as_view()),
    path('verify-ResendOTPView/',VerifyResendOTPView.as_view()),
    path('Otp-ForgotPassword/',ResendOtpForgotPassword.as_view()),
     path('Newpassword-changing/',ChangeNewPassword.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(),  name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),  name ='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('resend-otp/', ResendOtp.as_view(), name='resend-otp'),
    path('check-otp-verified/', Check_Otp.as_view(), name='check-confirmation'),


]
