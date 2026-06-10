from notes.storage import InMemoryStorage

# Test cases for the InMemoryStorage class,
# verifying note addition, retrieval, and deletion functionality
def test_add_and_get_note():
    storage = InMemoryStorage()
    storage.add_note("Test")
    notes = storage.get_all_notes()
    assert len(notes) == 1
    assert notes[0].content == "Test"

def test_delete_note():
    storage = InMemoryStorage()
    storage.add_note("Delete me")
    storage.delete_note(1)
    assert storage.get_all_notes() == []