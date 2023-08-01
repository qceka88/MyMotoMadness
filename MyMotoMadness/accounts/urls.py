from django.urls import path

from MyMotoMadness.accounts.views import RegisterMotoUser, LoginMotoUserView, LogoutMotoUserView, DetailsMotoUserView

# Accounts URLS
urlpatterns = [
    path('register/', RegisterMotoUser.as_view(), name='register user view'),
    path('login/', LoginMotoUserView.as_view(), name='login user view'),
    path('logout/', LogoutMotoUserView.as_view(), name='logout user view'),
    path('details/<int:pk>/', DetailsMotoUserView.as_view(), name='details user view'),
]
