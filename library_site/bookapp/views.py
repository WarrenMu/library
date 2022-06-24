from django.shortcuts import render

# Create your views here.

#shared views
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

