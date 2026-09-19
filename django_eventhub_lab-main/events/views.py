from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Event, Registration

def event_list(request):
    # TODO: Query Event objects with the ORM.
    # Order by event_date.
    # Optionally filter by GET parameters:
    # category and status.
    events=[]
    # TODO: Query all Category objects for the filter form.
    return render(request,"events/event_list.html",{"events":events})

def event_detail(request,event_id):
    # TODO: Retrieve the Event with get_object_or_404().
    event=None
    # TODO: Retrieve event.registrations.all().
    registrations=[]
    return render(request,"events/event_detail.html",{
        "event":event,"registrations":registrations
    })

@login_required
def register_event(request,event_id):
    # TODO: Retrieve the event.
    # TODO: Only register on POST.
    # TODO: Use request.user.
    # TODO: Prevent duplicate registrations.
    return redirect("events:event_detail",event_id=event_id)

@permission_required("events.add_event",raise_exception=True)
def create_event(request):
    # TODO: On GET, show categories.
    # TODO: On POST, create Event using request.POST and request.user.
    return render(request,"events/event_form.html")

@permission_required("events.change_event",raise_exception=True)
def edit_event(request,event_id):
    # TODO: Retrieve event.
    # TODO: On POST, update fields and save().
    return render(request,"events/event_form.html")

@permission_required("events.delete_event",raise_exception=True)
def delete_event(request,event_id):
    # TODO: Retrieve event.
    # TODO: Delete only after POST.
    return redirect("events:event_list")

def user_login(request):
    # TODO: Authentication task:
    # 1. Check POST.
    # 2. Read username/password.
    # 3. Call authenticate().
    # 4. If successful, call login(request,user).
    # 5. Redirect to event_list.
    # 6. Otherwise show an error.
    return render(request,"events/login.html")

def user_logout(request):
    # TODO: Call logout(request), then redirect to login.
    return redirect("events:login")
