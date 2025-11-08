def linear_search_recursive(arr, target, index=0):
    print(f"{index}, {target}, {arr[index]}")
    if index == len(arr):
        return -1 
    if arr[index] == target:
        return index
    
    # Recursive call to check the next element
    return linear_search_recursive(arr, target, index + 1)

# Example
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search_recursive(arr, target)

"""if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")"""
print ({result})

    