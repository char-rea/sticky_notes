from django import forms
from .models import StickyNote

# form class for creating and updating sticky notes, 
# based on the StickyNote model
class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'content']