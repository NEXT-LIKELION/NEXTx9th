import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.shortcuts import render, redirect
from app.models import Post, Comment, Chatroom, Chat
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime
from account.models import Profile, Lecture, PLR

# Create your views here.

###################### board ############################

def board(request, lecture_pk):
    lecture = Lecture.objects.get(subnum=lecture_pk)
    posts = Post.objects.filter(lecture=lecture)

    return render(request, '3_board/board.html', { 'posts': posts, 'lecture': lecture })



@login_required(login_url='account/login')
def new(request, lecture_pk):
    lecture = Lecture.objects.get(subnum=lecture_pk)
    if request.method == 'POST':
        new_post = Post.objects.create(
            lecture = lecture,
            author = request.user.profile,
            title = request.POST['title'],
            content = request.POST['content'],
            created_at = datetime.datetime.now(),
        )
        return redirect('detail', lecture_pk, new_post.pk)
    return render(request, '3_board/new.html', {'lecture_pk': lecture_pk })

def detail(request, lecture_pk, post_pk):
    lecture = Lecture.objects.get(subnum=lecture_pk)
    post = Post.objects.get(pk=post_pk)

    if (request.method == 'POST'):
        Comment.objects.create(
            post = post, 
            content = request.POST['content'],
            author = request.user.profile,
            created_at = datetime.datetime.now()
        )
        return redirect('detail', lecture_pk, post_pk)

    return render(request, '3_board/detail.html', {'post': post, 'lecture_pk': lecture_pk})

def delete(request, lecture_pk, post_pk):
    post = Post.objects.get(pk=post_pk)
    Post.objects.filter(pk=post_pk).update(
        title = "펑",
        content = "펑"
    )
    return redirect('detail', lecture_pk, post_pk)


def delete_comment(request, lecture_pk, post_pk, comment_pk):
    comment = Comment.objects.filter(pk=comment_pk)
    comment.update(
        content = "펑"
    )
    return redirect('detail', lecture_pk, post_pk)

########################################################

############### chatting ##############

def friend_profile(request, friend_pk):
    friend = Profile.objects.get(pk=friend_pk)
    plrs = PLR.objects.filter(profile=friend)

    return render(request, '4_chat/friend_profile.html', {'friend': friend, 'plrs': plrs})

def friends(request, lecture_pk):
    lecture = Lecture.objects.get(subnum=lecture_pk)
    admin = User.objects.get(username='admin').profile
    plrs = PLR.objects.filter(lecture=lecture).exclude(profile=request.user.profile).exclude(profile=admin)

    return render(request, '4_chat/friends.html', {'plrs': plrs, 'lecture': lecture})

def makeroom(request, friend_pk):
    find_room = Chatroom.objects.filter(profile1 = request.user.profile).filter(profile2 = Profile.objects.get(pk=friend_pk))
    if not (find_room):
        find_room = Chatroom.objects.filter(profile2 = request.user.profile).filter(profile1 = Profile.objects.get(pk=friend_pk))
    
    if not (find_room):
        new_room = Chatroom.objects.create(
            profile1 = request.user.profile,
            profile2 = Profile.objects.get(pk=friend_pk)
        )
        return redirect('chatroom', new_room.pk, friend_pk)
    
    return redirect('chatroom', find_room[0].pk, friend_pk)



def chatroom(request, room_pk, friend_pk):
    room = Chatroom.objects.get(pk=room_pk)
    chats = Chat.objects.filter(chatroom=room).order_by('created_at')
    friend = Profile.objects.get(pk=friend_pk)
    chats.filter(pfrom=friend).filter(read=False).update(
        read=True
    )


    if (request.method=='POST'):
        new_chat = Chat.objects.create(
            pfrom = request.user.profile,
            pto = Profile.objects.get(pk=friend_pk),
            content = request.POST['content'],
            created_at = datetime.datetime.today(),
            chatroom = room
        )
        return redirect('chatroom', room_pk, friend_pk)

    return render(request, '4_chat/chatroom.html', {'room': room, 'chats': chats, 'friend': friend})
#######################################