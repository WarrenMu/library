from multiprocessing import context
from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Lets learn c/c++'},
#     {'id':3, 'name':'Lets learn Assembly'},

# ]

def loginPage(request):

    if request.method == 'POST':
        username = request.get('username')
        username = request.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            



    context ={}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics':topics, 'room-count':room_count}
    return render(request, 'base/home.html', context)




def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)



def createRoom(request):
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def updatedRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method =='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={}



    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
