class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to display course head office location    
    def head_office_location(self):
        print("Our head office is located in Cape Town, South Africa")

#subclass of course class name OOPCourse
class OOPCourse(Course):
    pass

#create a constructor
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

#method in the OOPCourse subclass
    def trainer_details(self):
        print(f"This course is about {self.description} and is taught by {self.trainer}.")

 #method in the OOPCourse subclass named show_course_id that prints the ID number of the course: #12345
    def show_course_id(self):
        print("The course ID is: #12345")

#object of the OOPCourse subclass
course_1 = OOPCourse()
course_1.contact_details()
course_1.head_office_location()
course_1.trainer_details()
course_1.show_course_id()