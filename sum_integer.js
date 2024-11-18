// Two Sum Solution in JavaScript
function twoSum(nums, target) {
    // Create a map to store numbers and their indices
    let numMap = new Map();

    // Loop through the array
    for (let i = 0; i < nums.length; i++) {
        // Calculate the complement needed to reach the target
        let complement = target - nums[i];

        // Check if the complement is already in the map
        if (numMap.has(complement)) {
            // Return the indices of the two numbers
            return [numMap.get(complement), i];
        }

        // If not found, store the current number and its index in the map
        numMap.set(nums[i], i);
    }

    // If no solution exists (not expected per problem constraints)
    throw new Error("No solution found");
}

// Example usage:
console.log(twoSum([2, 7, 11, 15], 9)); // Output: [0, 1]
