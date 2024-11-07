// Function to check if a string is a palindrome
function isPalindrome(str) {
    // Step 1: Convert the string to lowercase to make it case-insensitive
    str = str.toLowerCase();
  
    // Step 2: Remove any spaces or non-alphanumeric characters (optional, based on requirement)
    str = str.replace(/[^a-z0-9]/g, '');
  
    // Step 3: Check if the string is equal to its reverse
    let reversedStr = str.split('').reverse().join(''); // Reverse the string
  
    // Step 4: Compare the original and reversed strings
    return str === reversedStr; // Return true if palindrome, else false
  }
  
  // Example Usage
  console.log(isPalindrome("madam")); // True
  console.log(isPalindrome("hello")); // False
  