from django.urls import path, include

from MyMotoMadness.messagebox.views import ReceivedMessagesView, SentMessagesView, SendMessageView, \
    DetailReceivedMessageView, DetailSentMessageView, DeleteMessageView, CreateNewMessageView

urlpatterns = [
    path('', include([
        path('message-box/', include([
            path('received/', include([
                path('', ReceivedMessagesView.as_view(), name='received list messages view'),
                path('details/<str:slug>/', DetailReceivedMessageView.as_view(), name='detail received message view'),
            ])),
            path('sent/', include([
                path('', SentMessagesView.as_view(), name='sent list messages view'),
                path('details/<str:slug>/', DetailSentMessageView.as_view(), name='detail sent message view'),
            ])),
        ])),
        path('create_message/', CreateNewMessageView.as_view(), name='create new message view'),
        path('send_message/<int:pk>/', SendMessageView.as_view(), name='send message view'),
        path('delete-message/<str:slug>/', DeleteMessageView.as_view(), name='delete message view'),
    ])),
]
