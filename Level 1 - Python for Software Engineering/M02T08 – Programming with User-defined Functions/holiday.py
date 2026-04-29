#calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost

destination = input("Welcome to the Holiday Cost Calculator! Let's calculate your total holiday cost.\nFirst, what is the destination? You can choose from Melbourne, Perth, Sydney, or other locations.\n")
nights = int(input("How many nights will you be staying?\n"))
car = int(input("How many days will you be renting a car?\n"))

#plane cost is determined by the destination, hotel cost is $150 per night, and car rental is $40 per day. We will create a function for each of these costs and then a final function to calculate the total cost of the holiday.
def plane_cost(destination):
    if destination.lower() == "melbourne":
        return 1200
    elif destination.lower() == "perth":
        return 1000
    elif destination.lower() == "sydney":
        return 1500
    else:
        return 800

def hotel_cost(nights):
    return nights * 150 

def car_rental(car):
    return car * 40

#total cost calculated by adding the plane cost, hotel cost, and car rental cost together
def holiday_cost(destination, nights, car):
    total = plane_cost(destination) + hotel_cost(nights) + car_rental(car)
    return total
total = holiday_cost(destination, nights, car)

#print our full details of the holiday and the total cost to the user
print(f"How exciting, you are going to {destination}! The plane trip costs ${plane_cost(destination)}.\nYou have a {nights} nights stay, costing ${hotel_cost(nights)} and will be renting a car for {car} days, costing ${car_rental(car)}. \nThe total cost of your holiday will be: ${total}. Have Fun!!")