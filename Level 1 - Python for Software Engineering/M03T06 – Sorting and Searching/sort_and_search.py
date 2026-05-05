#Implement this search algorithm to search for the number 9. Add a comment to explain why you think this algorithm was a good choice

numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

#linear search is a good choice for this algorithm.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1   

result = linear_search(numbers, 9)
print(result)

if result != -1:
    print(f"Linear Search: Found 9 at index {result}")
else:
    print("Linear Search: 9 not found")

#Binary Search (new algorithm on sorted list)
sorted_numbers = sorted(numbers)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

result = binary_search(sorted_numbers, 9)

if result != -1:
    print(f"Binary Search: Found 9 at index {result} in the sorted list")