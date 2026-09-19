from django.urls import path
from . import views
app_name="events"

urlpatterns=[
    path("", views.event_list, name="event_list"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("event/<int:event_id>/register/", views.register_event, name="register_event"),
    path("create/", views.create_event, name="create_event"),
    path("event/<int:event_id>/edit/", views.edit_event, name="edit_event"),
    path("event/<int:event_id>/delete/", views.delete_event, name="delete_event"),
]
