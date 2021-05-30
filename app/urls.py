from django.urls import path
from app import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #board
    path('board/<str:lecture_pk>', views.board, name="board"),
    path('new/<str:lecture_pk>', views.new, name="new"),
    path('detail/<str:lecture_pk>/<int:post_pk>', views.detail, name="detail"),
    path('delete/<str:lecture_pk>/<int:post_pk>', views.delete, name="delete"),
    path('delete_comment/<str:lecture_pk>/<int:post_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),

    #chatting
    path('friends/<str:lecture_pk>', views.friends, name="friends"),
    path('friend_profile/<int:friend_pk>', views.friend_profile, name="friend_profile"),
    path('makeroom/<int:friend_pk>', views.makeroom, name="makeroom"),
    path('chatroom/<int:room_pk>/<int:friend_pk>', views.chatroom, name="chatroom"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
