from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .models import CSEvent
from .models import ITEvent
from .models import EXTCEvent
from .models import INSTRUEvent
from .models import KEvent
from .models import SEvent
from .models import AEvent
from .models import GEvent
import json
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

def home(request): 
    return render(request, "home/home.html")

def index(request):
    event_list = Event.objects.all()
    all_events = []
    print(event_list)
    for event in event_list: 
        if(event.time):
            event.time = event.time.timestamp() * 1000
            sample_event = {
                "name": event.name,
                "time": event.time,
                "desc": event.desc
            }


            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})




def CS(request):
    event_list = CSEvent.objects.all()
    all_events = []
    print(event_list)
    for csevent in event_list:
        if(csevent.time):
            csevent.time = csevent.time.timestamp() * 1000
            sample_event = {
                "name": csevent.name,
                "time": csevent.time,
                "desc": csevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def IT(request):
    event_list = ITEvent.objects.all()
    all_events = []
    print(event_list)
    for itevent in event_list:
        if(itevent.time):
            itevent.time = itevent.time.timestamp() * 1000
            sample_event = {
                "name": itevent.name,
                "time": itevent.time,
                "desc": itevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def EXTC(request):
    event_list = EXTCEvent.objects.all()
    all_events = []
    print(event_list)
    for extcevent in event_list:
        if(extcevent.time):
            extcevent.time = extcevent.time.timestamp() * 1000
            sample_event = {
                "name": extcevent.name,
                "time": extcevent.time,
                "desc": extcevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def INSTRU(request):
    event_list = INSTRUEvent.objects.all()
    all_events = []
    print(event_list)
    for instruevent in event_list:
        if(instruevent.time):
            instruevent.time = instruevent.time.timestamp() * 1000
            sample_event = {
                "name": instruevent.name,
                "time": instruevent.time,
                "desc": instruevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})


def KALARAAG(request):
    event_list = KEvent.objects.all()
    all_events = []
    print(event_list)
    for kevent in event_list:
        if(kevent.time):
            kevent.time = kevent.time.timestamp() * 1000
            sample_event = {
                "name": kevent.name,
                "time": kevent.time,
                "desc": kevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def SUC(request):
    event_list = SEvent.objects.all()
    all_events = []
    print(event_list)
    for sevent in event_list:
        if(sevent.time):
            sevent.time = sevent.time.timestamp() * 1000
            sample_event = {
                "name": sevent.name,
                "time": sevent.time,
                "desc": sevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def ACM(request):
    event_list = AEvent.objects.all()
    all_events = []
    print(event_list)
    for aevent in event_list:
        if(aevent.time):
            aevent.time = aevent.time.timestamp() * 1000
            sample_event = {
                "name": aevent.name,
                "time": aevent.time,
                "desc": aevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def GDSC(request):
    event_list = GEvent.objects.all()
    all_events = []
    print(event_list)
    for gevent in event_list:
        if(gevent.time):
            gevent.time = gevent.time.timestamp() * 1000
            sample_event = {
                "name": gevent.name,
                "time": gevent.time,
                "desc": gevent.desc
            }
            all_events.append((sample_event))
    return render(request, "index.html", {'event_list':all_events})

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        # print(request.POST['loginpassword'])
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        print(loginusername, loginpassword)
        user=authenticate(request, username = loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('home')

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        print(username, email, fname, lname, pass1)

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        print(myuser)
        messages.success(request, "Your RAIT Calendar has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
    

    return HttpResponse("login")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")



