#program to manipulate floats using built-in functions.
import statistics

numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num) 

total = sum(numbers)
print(f"The total of all the numbers is: {total}")

max_index = numbers.index(max(numbers))
print(f"The index of the maximum number is: {max_index}")

min_index = numbers.index(min(numbers))
print(f"The index of the minimum number is: {min_index}")

average = round(sum(numbers) / len(numbers), 2)
print(f"The average (mean) of the numbers is: {average}")

median = statistics.median(numbers)
print(f"The median number is: {median}")