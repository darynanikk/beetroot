from django.contrib import admin
from django.urls import path, include
from notes.views import home_page

urlpatterns = [
    path("notes/", include("notes.urls")),
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    path("", include("users.urls")),
    path("", include('django.contrib.auth.urls'))
]
