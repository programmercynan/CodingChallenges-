# Two Sum Solution in Python
def two_sum(nums, target):
    # Create a dictionary to store numbers and their indices
    num_map = {}

    # Loop through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]

        # If not found, store the current number and its index in the dictionary
        num_map[num] = i

    # If no solution exists (not expected per problem constraints)
    raise ValueError("No solution found")

# Example usage:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
