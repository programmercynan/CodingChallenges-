def lengthOfLongestSubString(s: str) -> int:
    # create a set to store unique characters
    char_set = set()

    # initialize the start pointer and max length 
    start = 0
    max_len = 0

    # iterate over the string with the 'end' pointer 
    for end in range(len(s)):
        # if the character is already in the set, shrink the window from the start
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1

            # add the current character to the set 
            char_set.add(s[end])