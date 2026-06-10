from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm


def note_list(request):
    """
    View to list all sticky notes.

    Retrieves all sticky notes from the database and renders them in the
    'note_list.html' template.
    """
    notes = StickyNote.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_create(request):
    """
    View to create a new sticky note.

    If the request method is POST, it processes the form data and saves the
    new note. If the request method is GET, it displays an empty form.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = StickyNoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    View to update an existing sticky note by ID.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    form = StickyNoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect("note_list")

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    Delete a sticky note by ID.

    If the request method is POST, the note is deleted and the user is
    redirected to the note list.
    """
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note},
    )