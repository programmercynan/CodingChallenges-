def lengthOfLongestSubString(s: str) -> int:
    # create a set to store unique characters
    char_set = set()

    # initialize the start pointer and max length 
    start = 0
    max_len = 0