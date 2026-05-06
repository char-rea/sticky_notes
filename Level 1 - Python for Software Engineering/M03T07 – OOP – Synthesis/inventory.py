#Nike stock inventory management system to view, add, restock, search
# and calculate the value of shoes in stock.

#========The beginning of the class==========

class Shoe: 
    """Class Shoe is used to store data about a shoe, including country, code, product, cost and quantity."""


# Define the init function and 5 attributes:
# Country, code, product, cost and quantity.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)


# Define the functions cost, quantity to return each attribute:
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# Shoe_list will be used to store a list of shoes objects.
shoe_list = []


#==========Functions outside the class==============

# Read the shoe data from the inventory.txt file
# The data from the file will be used to create shoe objects 
# And append them to the shoe list.
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line

            for line in file:
                data = line.strip().split(",")
                shoe = Shoe(*data)
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


# Define the function capture_shoes() which will allow a user to capture data
def capture_shoes():
    """This function captures shoe data from the user and
    creates a shoe object, which is then added to the shoe list."""
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)


# Define the function view_all() which will iterate over 
# The shoes list and print the details of the shoes 
# Returned from the __str__ function
def view_all():
    for shoe in shoe_list:
        print(shoe)


# Define the function re_stock() which will find the shoe 
# Object with the lowest quantity and if it needs to be restocked.
def re_stock():
    lowest = min(shoe_list, key=lambda x: x.quantity)

    print("The lowest stock item is:")
    print(lowest)

    choice = input("Do you want to restock this item? (yes/no): ")

    if choice.lower() == "yes":
        add_qty = int(input("Please enter quantity to add: "))
        lowest.quantity += add_qty


# Update file to show new stock level
        update_file()

# Write back to the file after restocking
def update_file():
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


# Define the function search_shoe() which
# Will search for a shoe from the list using the shoe code and return.
def search_shoe():

    code = input("Enter shoe code: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return

    print("Shoe not found.")


# Define the function value_per_item() which 
# Will calculate the total value for each item.
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} value: {value}")


# define the function highest_qty() which will 
# Determine the product with the highest quantity.
def highest_qty():

    highest = max(shoe_list, key=lambda x: x.quantity)

    print("Item for sale:")
    print(highest)


#==========Main Menu=============

# This menu will be used to display the options 
# To the user and to capture the user's selection. 
# The menu will be displayed until the user decides to exit.
read_shoes_data()

while True:
    print("\nWelcome to the Nike Shoe Inventory Menu, please make a selection from the options below:")
    print("1. View all shoes")
    print("2. Add new shoes")
    print("3. Restock")
    print("4. Search shoes")
    print("5. View Value per item")
    print("6. Highest quantity item for sale")
    print("0. Exit")

    choice = input("Enter your choice using the menu number: ")

    if choice == "1":
        view_all()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "0":
        break
    else:
        print("Invalid choice.")