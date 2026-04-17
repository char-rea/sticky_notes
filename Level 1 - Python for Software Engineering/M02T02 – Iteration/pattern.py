#output code for an arrow pattern, using if statements to determine which character to print

rows = 5

for i in range(1, rows * 2 - 1):
    if i <= rows:
        print("*" * i)        
    else:
        print("*" * (rows * 2 - i))