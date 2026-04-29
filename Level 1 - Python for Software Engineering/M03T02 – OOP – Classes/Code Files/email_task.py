"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
#create class
class Email():
    
# Initialise the instance variables for each email.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False #initially set to false as the email has not been read yet

# Create the 'mark_as_read()' method to change the 'has_been_read'
    def mark_as_read(self):
        self.has_been_read = True #instance variable for a specific object from False to True.

#an empty variable called inbox of type list to store and access the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    inbox.append(Email("hannah@hello.com", "Im happy", "Happy is fun! Great stuff"))
    inbox.append(Email("max@hello.com", "Im excited", "Excited is the best! Woohoo"))
    inbox.append(Email("george@hello.com", "Im sad", "Sad is not fun!"))


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for i, email in enumerate(inbox):
        print(f"{i} {email.subject_line}")


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email index.")

def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    unread_emails = [email for email in inbox if not email.has_been_read]
    for i, email in enumerate(unread_emails):
        print(f"{i} {email.subject_line}")


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.


# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Quitting application.")
        break

    else:
        print("Oops - incorrect input.")
