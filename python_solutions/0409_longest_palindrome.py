# Link: https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s):
    # key: unique character
    # value: number of times said character occurs in s
    char_count = {}
    
    # Populate the char_count dictionary
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    palindrome = 0 # Length of the longest palindrome
    odd = False # Whether there's at least one odd num occ char
    
    for count in char_count.values():
        # Case 1: The current character occurs an odd number of times
        if count%2 != 0:
            odd = True # Set odd flag
            # Add an even number of those characters
            palindrome += (count-1)
        # Case 2: The current character occurs an even number of times
        else:
            palindrome += count
    
    # If we encountered at least one oddly occuring character
    if odd:
        # Add 1 since you can have an odd number of chars in the middle
        # of the palindrome
        palindrome += 1
    
    return palindrome