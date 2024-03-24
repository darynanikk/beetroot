from django.forms import ModelForm, CheckboxSelectMultiple
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Note


class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text", "reminder", "categories"]
        widgets = {
            "categories": CheckboxSelectMultiple(),
            "reminder": DateTimePickerInput()
        }