# list called menu and dictionary: stock and price list that should contain at least four items sold in the café. 

menu = ["coffee", "hot chocolate", "matcha", "cake"]

stock = {
    'coffee': 50,
    'hot chocolate': 30,
    'matcha': 20,
    'cake': 15
}

prices = {
    'coffee': 2.50,
    'hot chocolate': 1.50,
    'matcha': 3.00,
    'cake': 3.00
}

total_value = 0
for item in menu:
    item_value = stock[item] * prices[item]
    total_value += item_value

print("Menu:", menu)
print("Stock:", stock)
print("Prices:", prices)    
print("Total value of stock:", total_value)