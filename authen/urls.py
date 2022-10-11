from django.urls import path
from authen.views import Logout, CustomLogin, CustomSignUp

urlpatterns = [
    path('login', CustomLogin.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('signup', CustomSignUp.as_view(), name="signup"),
]
