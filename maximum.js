// Function to find the maximum value in an array
function findMax(arr) {
    // Handle edge case: empty array
    if (arr.length === 0) {
        throw new Error("Array is empty. Cannot find maximum value.");
    }

    // Initialize the maximum value with the first element of the array
    let max = arr[0];

    // Loop through the array to find the maximum
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]; // Update max if the current element is greater
        }
    }

    return max; // Return the maximum value
}

// Example usage:
console.log(findMax([3, 1, 4, 1, 5, 9])); // Output: 9
