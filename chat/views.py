from django.shortcuts import render

# Function to return HTML-view
def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

