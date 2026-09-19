from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES=[
        ("upcoming","Upcoming"),("ongoing","Ongoing"),("finished","Finished")
    ]
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    location=models.CharField(max_length=200)
    event_date=models.DateTimeField()

    # TODO: Add Category ForeignKey.
    # Use related_name="events".
    # category = ...

    # TODO: Add User ForeignKey for the organizer.
    # Use related_name="created_events".
    # organizer = ...

    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="upcoming")
    capacity=models.PositiveIntegerField(default=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # TODO: Return the event title.
        return "TODO"

class Registration(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="registrations")

    # TODO: Add User ForeignKey.
    # Use related_name="event_registrations".
    # user = ...

    registered_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        # TODO: Prevent duplicate registrations for the same user/event.
        # constraints = [...]
        pass

    def __str__(self):
        # TODO: Return useful information.
        return "TODO"
