#calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost

destination = input("Welcome to the Holiday Cost Calculator! Let's calculate your total holiday cost.\nFirst, what is the destination?\n")
nights = int(input("How many nights will you be staying?\n"))
car = int(input("How many days will you be renting a car?\n"))

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

def car_rental_cost(car):
    return car * 40

def total_cost(destination, nights, car):
    total = plane_cost(destination) + hotel_cost(nights) + car_rental_cost(car)
    return total
total = total_cost(destination, nights, car)
print(f"The total cost of your holiday to {destination} is: ${total}")