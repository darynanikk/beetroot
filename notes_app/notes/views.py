from django.shortcuts import render
from .models import Note


# Create your views here.
def index(request):
    latest_notes = Note.objects.order_by("-reminder")[:5]
    return render(request, "notes/notes.html",
                  {"latest_notes": latest_notes})
