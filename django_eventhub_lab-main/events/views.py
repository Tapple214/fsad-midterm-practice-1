from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Event, Registration

def event_list(request):
    events = Event.objects.all().order_by("event_date")
    category = request.GET.get("category")
    status = request.GET.get("status")
    if category:
        events = events.filter(category_id=category)
    if status:
        events = events.filter(status=status)
    categories = Category.objects.all()
    return render(request, "events/event_list.html", {"events": events, "categories": categories})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrations = event.registrations.all()
    return render(request, "events/event_detail.html", {
        "event": event, "registrations": registrations
    })

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        if not Registration.objects.filter(event=event, user=request.user).exists():
            Registration.objects.create(event=event, user=request.user)
    return redirect("events:event_detail", event_id=event_id)

@permission_required("events.add_event", raise_exception=True)
def create_event(request):
    categories = Category.objects.all()
    if request.method == "POST":
        Event.objects.create(
            title=request.POST["title"],
            description=request.POST.get("description", ""),
            location=request.POST["location"],
            event_date=request.POST["event_date"],
            category_id=request.POST["category"],
            status=request.POST.get("status", "upcoming"),
            capacity=int(request.POST.get("capacity", 50)),
            organizer=request.user,
        )
        return redirect("events:event_list")
    return render(request, "events/event_form.html", {"categories": categories})

@permission_required("events.change_event", raise_exception=True)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    categories = Category.objects.all()
    if request.method == "POST":
        event.title = request.POST["title"]
        event.description = request.POST.get("description", "")
        event.location = request.POST["location"]
        event.event_date = request.POST["event_date"]
        event.category_id = request.POST["category"]
        event.status = request.POST.get("status", event.status)
        event.capacity = int(request.POST.get("capacity", event.capacity))
        event.save()
        return redirect("events:event_detail", event_id=event_id)
    return render(request, "events/event_form.html", {"event": event, "categories": categories})

@permission_required("events.delete_event", raise_exception=True)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.delete()
        return redirect("events:event_list")
    return render(request, "events/delete_event.html", {"event": event})

def user_login(request):
    error = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("events:event_list")
        error = "Invalid username or password."
    return render(request, "events/login.html", {"error": error})

def user_logout(request):
    logout(request)
    return redirect("events:login")
