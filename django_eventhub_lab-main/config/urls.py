from django.contrib import admin
from django.urls import include, path

urlpatterns=[
    path("admin/",admin.site.urls),
    # TODO: Include events.urls at the root URL.
    # path("",include("events.urls")),
]
