from django.test import TestCase
from notes.models import StickyNote

# Test cases for the StickyNote model, 
# verifying creation and deletion functionality
class StickyNoteTests(TestCase):

    def test_create_note(self):
        note = StickyNote.objects.create(content="Test note")
        self.assertEqual(note.content, "Test note")

    def test_delete_note(self):
        note = StickyNote.objects.create(content="Delete me")
        note.delete()
        self.assertEqual(StickyNote.objects.count(), 0)