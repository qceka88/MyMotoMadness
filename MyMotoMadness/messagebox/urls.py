from django.urls import path, include

from MyMotoMadness.messagebox.views import ReceivedMessagesView, SentMessagesView, SendMessageView, DetailsMessageView, \
    DeleteMessageView

urlpatterns = [
    path('', include([
        path('message-box/', include([
            path('received/', ReceivedMessagesView.as_view(), name='received messages view'),
            path('sent/', SentMessagesView.as_view(), name='sent messages view'),
        ])),
        path('create_message/', SendMessageView.as_view(), name='create new message view'),
        path('send_message/<int:pk>/', SendMessageView.as_view(), name='send message view'),
        path('details-message/<str:slug>/', DetailsMessageView.as_view(), name='detail message view'),
        path('delete-message/<str:slug>/', DeleteMessageView.as_view(), name='delete message view'),
    ])),
]
