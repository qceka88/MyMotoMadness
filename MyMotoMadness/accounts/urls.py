from django.urls import path

from MyMotoMadness.accounts.views import RegisterMotoUser

# Accounts URLS
urlpatterns = [
    path('register/', RegisterMotoUser.as_view(), name='register user view'),
]
