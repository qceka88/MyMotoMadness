from django.urls import path

from MyMotoMadness.messagebox.views import MessageBoxListView, SendMessageView

# TODO: Test crud actions.
# TODO: Include messages URLS to user details URL
urlpatterns = [
    path('messages/', MessageBoxListView.as_view(), name='list messages view'),
    path('create_message/<int:pk>/', SendMessageView.as_view(), name='send message view'),
]
