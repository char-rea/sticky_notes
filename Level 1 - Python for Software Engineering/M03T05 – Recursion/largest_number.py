#find the largest number in the list

def largest_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    max_of_rest = largest_number(numbers[:-1])
    
    if numbers[-1] > max_of_rest:
        return numbers[-1]
    else:
        return max_of_rest
    
#Example usage
if __name__ == "__main__":
    print(largest_number([1, 4, 5, 3])) # Output: 5
    print(largest_number([3, 1, 6, 8, 2, 4, 5])) # Output: 8
