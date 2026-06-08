``` # A bookstore DMS using SQLite.
# This program allows users to manage a bookstore inventory 
# by performing various operations such as adding new books, 
# updating existing book details, deleting books, searching 
# for specific books, and viewing the details of all books 
# in the inventory. 


# --- Imports ---

import sqlite3


# --- Database Setup ---

DATABASE_NAME = 'ebookstore.db'


# --- Create Table ---

def create_tables():
    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    authorID INTEGER NOT NULL,
                    qty INTEGER NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS author(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    country TEXT NOT NULL
                )
            """)
    except sqlite3.Error as e:
        print("Database error:", e)


# Insert initial data into the book table
def populate_tables():
    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()

            books = [
                (3001, "A Tale of Two Cities", 1290, 30),
                (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
                (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
                (3004, "The Lord of the Rings", 6380, 37),
                (3005, "Alice's Adventures in Wonderland", 5620, 12)
            ]

            cursor.executemany(
                "INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)",
                books
            )

            authors = [
                (1290, "Charles Dickens", "England"),
                (8937, "J.K. Rowling", "England"),
                (2356, "C.S. Lewis", "Ireland"),
                (6380, "J.R.R. Tolkien", "South Africa"),
                (5620, "Lewis Carroll", "England")
            ]

            cursor.executemany(
                "INSERT OR IGNORE INTO author VALUES (?, ?, ?)",
                authors
            )
    except sqlite3.Error as e:
        print("Database error:", e)


# --- Validation check ---

def validate_input(prompt, expected_type):
    while True:
        user_input = input(prompt).strip()

        try:
            if expected_type == int:
                # Must be numeric
                if not user_input.isdigit():
                    raise ValueError

                # Convert to int
                value = int(user_input)

                # Enforce exactly 4 digits for IDs
                if "ID" in prompt and len(user_input) != 4:
                    print("ID must be exactly 4 digits.")
                    continue

                return value

            elif expected_type == str:
                if not user_input:
                    print("Input cannot be empty.")
                    continue
                return user_input

            else:
                print("Unsupported type.")
        except ValueError:
            print(f"Invalid input. Expected a {expected_type.__name__}.")

# --- Functions ---


# Add a new book with valid input
def enter_book():
    book_ID = validate_input("Enter book ID: ", int)
    title = validate_input("Enter book title: ", str)
    authorID = validate_input("Enter author ID: ", int)
    qty = validate_input("Enter quantity: ", int)

    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()

            cursor.execute("SELECT 1 FROM author WHERE id = ?", (authorID,))
            author_exists = cursor.fetchone()

            if not author_exists:
                name = validate_input("Enter author's name: ", str)
                country = validate_input("Enter author's country: ", str)
                cursor.execute(
                    "INSERT INTO author (id, name, country) VALUES (?, ?, ?)",
                    (authorID, name, country)
                )

            cursor.execute(
                "INSERT INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)",
                (book_ID, title, authorID, qty)
            )

        print("Book added successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)


# Update book details with valid input
def update_book():
    book_ID = validate_input("Enter book ID to update: ", int)

    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()

            # Check if book exists and fetch current details
            cursor.execute("""
                SELECT book.title,
                       book.authorID,
                       book.qty,
                       author.name,
                       author.country
                FROM book
                LEFT JOIN author ON book.authorID = author.id
                WHERE book.ID = ?
            """, (book_ID,))
            result = cursor.fetchone()

            if not result:
                print("Book not found.")
                return

            title, authorID, qty, author_name, author_country = result

            # Display current details
            print("\nCurrent details:")
            print("Title:", title)
            print("Author ID:", authorID)
            print("Author Name:", author_name)
            print("Author Country:", author_country)
            print("Quantity:", qty)

            # Update menu
            print("""
            What would you like to update?
            1. Quantity
            2. Title
            3. Author ID
            4. Author Name
            5. Author Country
            """)

            choice = validate_input("Select an option: ", int)

            if choice == 1:
                new_qty = validate_input("Enter new quantity: ", int)
                cursor.execute(
                    "UPDATE book SET qty = ? WHERE ID = ?",
                    (new_qty, book_ID)
                )

            elif choice == 2:
                new_title = validate_input("Enter new title: ", str)
                cursor.execute(
                    "UPDATE book SET title = ? WHERE ID = ?",
                    (new_title, book_ID)
                )

            elif choice == 3:
                new_authorID = validate_input("Enter new author ID: ", int)

                # Check if author exists
                cursor.execute(
                    "SELECT 1 FROM author WHERE id = ?",
                    (new_authorID,)
                )
                if not cursor.fetchone():
                    name = validate_input("Enter author's name: ", str)
                    country = validate_input("Enter author's country: ", str)
                    cursor.execute(
                        "INSERT INTO author (id, name, country) VALUES (?, ?, ?)",
                        (new_authorID, name, country)
                    )

                cursor.execute(
                    "UPDATE book SET authorID = ? WHERE ID = ?",
                    (new_authorID, book_ID)
                )

            elif choice == 4:
                new_name = validate_input("Enter new author name: ", str)
                cursor.execute(
                    "UPDATE author SET name = ? WHERE id = ?",
                    (new_name, authorID)
                )

            elif choice == 5:
                new_country = validate_input("Enter new author country: ", str)
                cursor.execute(
                    "UPDATE author SET country = ? WHERE id = ?",
                    (new_country, authorID)
                )

            else:
                print("Invalid choice.")
                return

        print("Book updated successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)


# Delete book from the inventory with valid input
def delete_book():
    book_ID = validate_input("Enter book ID to delete: ", int)

    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()
            cursor.execute(
                "DELETE FROM book WHERE ID = ?",
                (book_ID,)
            )
        print("Book deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)


# Search for a book by ID and display its details
def search_book():
    book_ID = validate_input("Enter book ID: ", int)

    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()
            cursor.execute("""
                SELECT book.title, author.name, author.country, book.qty
                FROM book
                LEFT JOIN author ON book.authorID = author.id
                WHERE book.id = ?
            """, (book_ID,))
            row = cursor.fetchone()
    except sqlite3.Error as e:
        print("Database error:", e)
        return

    if row:
        title, author, country, qty = row
        print("Title:", title)
        print("Author:", author or "Unknown")
        print("Country:", country or "Unknown")
        print("Quantity:", qty)
    else:
        print("Book not found.")


# View all books in the inventory
def view_all_books():
    try:
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()
            cursor.execute("""
                SELECT book.title,
                       author.name,
                       author.country
                FROM book
                LEFT JOIN author
                ON book.authorID = author.id
            """)
            results = cursor.fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
        return

    print("\nDetails")
    for title, name, country in results:
        print("-" * 50)
        print("Title:", title)
        print("Author:", name or "Unknown")
        print("Country:", country or "Unknown")
    print("-" * 50)



# --- Main Program Loop ---

create_tables()
populate_tables()

while True:
    print("""
    Welcome to the Ebookstore Menu:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search book
    5. View details of all books
    6. Exit
    """)
    
    choice = validate_input("Please select an option: ", int)
    
    if choice == 1:
        enter_book()
    elif choice == 2:
        update_book()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        search_book()
    elif choice == 5:
        view_all_books()
        pass
    elif choice == 6:
        print("Goodbye! :)")
        break
    else:
        print("Invalid choice. Please try again.")
```