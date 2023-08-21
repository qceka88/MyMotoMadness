from django.urls import path, include

from MyMotoMadness.messagebox.views import MessageBoxListView, SendMessageView, DetailsMessageView, DeleteMessageView

# TODO: Test crud actions.
# TODO: Include messages URLS to user details URL
urlpatterns = [
    path('', include([
        path('message-box/', MessageBoxListView.as_view(), name='my message box view'),
        path('create_message/<int:pk>/', SendMessageView.as_view(), name='send message view'),
        path('details-message/<str:slug>/', DetailsMessageView.as_view(), name='detail message view'),
        path('delete-message/<str:slug>/', DeleteMessageView.as_view(), name='delete message view'),
    ])),
]
