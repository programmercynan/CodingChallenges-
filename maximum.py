# Function to find the maximum value in an array
def find_max(arr):
    # Handle edge case: empty array
    if len(arr) == 0:
        raise ValueError("Array is empty. Cannot find maximum value.")

    # Initialize the maximum value with the first element of the array
    max_val = arr[0]

    # Loop through the array to find the maximum
    for num in arr[1:]:
        if num > max_val:
            max_val = num  # Update max_val if the current element is greater

    return max_val  # Return the maximum value

# Example usage:
print(find_max([3, 1, 4, 1, 5, 9]))  # Output: 9
