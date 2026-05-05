#Modify the merge sort algorithm provided in the example usage section above to order a list of strings by string length from the longest to the shortest string.

#. Run the modified Merge sort algorithm against 3 string lists of your choice. Please ensure that each of your chosen lists is not sorted and has a length of at least 10 string elements.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) > len(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage
strings1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
strings2 = ["strawberry", "blueberry", "raspberry", "blackberry", "cranberry", "gooseberry", "boysenberry", "mulberry", "elderberry", "huckleberry"]
strings3 = ["watermelon", "cantaloupe", "honeydew", "papaya", "pineapple", "mango", "kiwi", "grapefruit", "orange", "lemon"]    

sorted_strings1 = merge_sort(strings1)
sorted_strings2 = merge_sort(strings2)
sorted_strings3 = merge_sort(strings3)

print("Sorted strings1 by length (longest to shortest):")
for string in sorted_strings1:
    print(string)
print("\nSorted strings2 by length (longest to shortest):")
for string in sorted_strings2:
    print(string)
print("\nSorted strings3 by length (longest to shortest):")
for string in sorted_strings3:
    
    print(string)
    
