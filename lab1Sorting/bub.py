def bubbleSortDescending(arr):
    """
    Sorts a list of numbers in descending order using the bubble sort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # If the current element is less than the next element, swap them
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                """ this is a test """
    return arr

# Example usage:
myList = [64, 34, 25, 12, 22, 11, 90]
sortedList = bubbleSortDescending(myList)
print(f"Original list: {myList}")
print(f"Sorted list (descending): {sortedList}")