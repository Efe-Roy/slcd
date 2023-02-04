from .views import SignupView
from django.urls import path, include
from .views import CustomAuthToken, user_detail, user_list

urlpatterns = [
    path('rest-auth/registration/', SignupView.as_view()),
    path('rest-auth/login/', CustomAuthToken.as_view(), name ='auth-token'),
    path('rest-auth/', include('rest_auth.urls')),

    path('user/', user_list),
    path('user/<int:pk>', user_detail),
]

