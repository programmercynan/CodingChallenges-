def lengthOfLongestSubstring(s: str) -> int:
    # Create a set to store unique characters
    char_set = set()
    
    # Initialize the start pointer and max length
    start = 0
    max_len = 0
    
    # Iterate over the string with the 'end' pointer
    for end in range(len(s)):
        # If the character is already in the set, shrink the window from the start
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        # Add the current character to the set
        char_set.add(s[end])
        
        # Update the max length if necessary
        max_len = max(max_len, end - start + 1)
    
    # Return the max length
    return max_len

# Test the function
input_string = "abcabcbb"
print(lengthOfLongestSubstring(input_string))  # Output: 3
