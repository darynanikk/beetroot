from django.contrib import admin
from django.urls import path
from .views import NoteListView, NoteCreateView, NoteDeleteView, NoteEditView

urlpatterns = [
    path("list", NoteListView.as_view(), name="index"),
    path("create", NoteCreateView.as_view(), name="create-note"),
    path("delete/<int:pk>", NoteDeleteView.as_view(), name="delete_note"),
    path("edit/<int:pk>", NoteEditView.as_view(), name="update_note")
]