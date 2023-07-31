from django.urls import path

from MyMotoMadness.accounts.views import RegisterMotoUser, LoginMotoUser, LogoutMotoUser

# Accounts URLS
urlpatterns = [
    path('register/', RegisterMotoUser.as_view(), name='register user view'),
    path('login/', LoginMotoUser.as_view(), name='login user view'),
    path('logout/', LogoutMotoUser.as_view(), name='logout user view'),
]
