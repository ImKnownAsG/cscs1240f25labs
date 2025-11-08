import random
import time

def max_subarray_naive(arr):
    """
    Implements the Naive (Brute-Force) approach for the Maximum Subarray Sum.
    Time Complexity: O(n^3) or optimized O(n^2).
    """
    n = len(arr)
    max_sum = float('-inf')  # Start with negative infinity
    start_index = -1
    end_index = -1

    # Outer loop: starting point of the subarray
    for i in range(n):
        current_sum = 0
        # Inner loop: ending point of the subarray
        for j in range(i, n):
            # Calculate the sum for the subarray arr[i...j]
            current_sum += arr[j]
            
            # Check if this subarray has a greater sum than the current max
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j
    
    # Return the maximum sum and the corresponding subarray
    return max_sum, arr[start_index : end_index + 1]


def max_subarray_kadane(arr):
    """
    Implements Kadane's Algorithm for the Maximum Subarray Sum.
    Time Complexity: O(n).
    """
    max_so_far = float('-inf')  # Overall maximum sum found
    current_max = 0             # Maximum sum ending at the current position
    
    # Variables to track the start/end indices of the max subarray
    start_index = 0
    end_index = 0
    current_start = 0

    # Iterate through the array once
    for i in range(len(arr)):
        # 1. Update current_max: Add the current element to the running sum
        current_max += arr[i]

        # 2. Check if the current_max is the new max_so_far
        if current_max > max_so_far:
            max_so_far = current_max
            start_index = current_start
            end_index = i
        
        # 3. Check if current_max drops below zero
        if current_max < 0:
            # Discard this sequence (since it drags down future sums)
            current_max = 0
            # Set the start of the next potential subarray to the next element
            current_start = i + 1
            
    # Handle the case where all numbers are negative (Kadane's default output is 0)
    # This modification finds the largest single element instead.
    if max_so_far == 0 and any(x < 0 for x in arr):
        max_so_far = max(arr)
        # Find index of the largest negative number
        start_index = arr.index(max_so_far)
        end_index = start_index

    return max_so_far, arr[start_index : end_index + 1]


# --- Main Execution ---

# Define the array (feel free to change this)
# A classic example with negative and positive numbers:
TEST_ARRAY = [4, -1, 2, -7, 3, 4, -2, 9, -10, 2, 5]

print("--- Maximum Subarray Sum Search ---")
print(f"Original Array: \n{TEST_ARRAY}\n")

# --- Naive Implementation ---
print("### 🐢 Naive (Brute-Force) O(n^2)")
start_time = time.time()
naive_sum, naive_subarray = max_subarray_naive(TEST_ARRAY)
end_time = time.time()

print(f"Max Sum: {naive_sum}")
print(f"Subarray: {naive_subarray}")
print(f"Time taken: {round((end_time - start_time) * 1000, 3)} ms")

print("\n" + "="*50 + "\n")

# --- Kadane's Implementation ---
print("### 🐇 Kadane's Algorithm O(n)")
start_time = time.time()
kadane_sum, kadane_subarray = max_subarray_kadane(TEST_ARRAY)
end_time = time.time()

print(f"Max Sum: {kadane_sum}")
print(f"Subarray: {kadane_subarray}")
print(f"Time taken: {round((end_time - start_time) * 1000, 3)} ms")