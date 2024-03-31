from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Note
from .forms import NoteCreateForm


class NoteListView(LoginRequiredMixin, ListView):
    context_object_name = "latest_notes"
    model = Note
    template_name = "notes/notes.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user).order_by("-reminder")[:5]
        return queryset


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteCreateForm
    template_name = "notes/note_create.html"

    def get_success_url(self):
        return reverse("index")


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note

    def get_success_url(self):
        return reverse("index")


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteCreateForm
    template_name = "notes/note_update.html"

    def get_success_url(self):
        return reverse("index")


def home_page(request):
    return render(request, "notes/home.html")