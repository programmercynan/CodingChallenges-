# Function to check if a string is a palindrome
def is_palindrome(s):
    # Step 1: Convert the string to lowercase to make it case-insensitive
    s = s.lower()

    # Step 2: Remove any spaces or non-alphanumeric characters (optional, based on requirement)
    s = ''.join(e for e in s if e.isalnum())

    # Step 3: Check if the string is equal to its reverse
    reversed_s = s[::-1]  # Reverse the string

    # Step 4: Compare the original and reversed strings
    return s == reversed_s  # Return True if palindrome, else False

# Example Usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
