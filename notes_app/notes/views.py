from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Note
from .forms import NoteCreateForm


class NoteListView(ListView):
    context_object_name = "latest_notes"
    queryset = Note.objects.order_by("-reminder")[:5]
    template_name = "notes/notes.html"


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm
    template_name = 'notes/note_create.html'

    def get_success_url(self):
        return reverse('index')


class NoteDeleteView(DeleteView):
    model = Note

    def get_success_url(self):
        return reverse('index')


class NoteEditView(UpdateView):
    model = Note
    form_class = NoteCreateForm
    template_name = 'notes/note_update.html'

    def get_success_url(self):
        return reverse('index')
