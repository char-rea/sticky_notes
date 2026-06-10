from django.test import TestCase
from django.urls import reverse
from notes.models import StickyNote

# Test cases for the StickyNote model and views, 
# covering full CRUD functionality.
class StickyNoteTests(TestCase):
    """
    Test cases for the StickyNote model and views,
    covering full CRUD functionality.
    """

    def test_create_note(self):
        """
        Test creating a sticky note directly via the model.
        """
        note = StickyNote.objects.create(
            title="Test Note",
            content="Test content"
        )
        self.assertEqual(note.content, "Test content")

    def test_delete_note(self):
        """
        Test deleting a sticky note.
        """
        note = StickyNote.objects.create(
            title="Delete Note",
            content="Delete me"
        )
        note.delete()
        self.assertEqual(StickyNote.objects.count(), 0)

    def test_view_notes(self):
        """
        Test viewing the list of sticky notes (READ use case).
        """
        StickyNote.objects.create(
            title="View Test",
            content="View content"
        )

        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test")

    def test_update_note(self):
        """
        Test updating an existing sticky note (UPDATE use case).
        """
        note = StickyNote.objects.create(
            title="Old Title",
            content="Old content"
        )

        response = self.client.post(
            reverse("note_update", args=[note.id]),
            {
                "title": "New Title",
                "content": "New content"
            }
        )

        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, "New Title")