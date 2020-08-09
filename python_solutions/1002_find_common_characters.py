# Link to problem: https://leetcode.com/problems/find-common-characters/

def commonChars(A):
    length = len(A)
    
    # Edge case: Only one string given; return all characters in it
    if length == 1:
        return list(A[0])
    
    # Dictionary to hold characters common amongst all strings
    common_chars = {}
    
    # Populate common_chars with the character count of the first word
    for char in A[0]:
        if char in common_chars:
            common_chars[char] += 1
        else:
            common_chars[char] = 1
    
    for i in range(1, length):
        curr_word = A[i]
        
        # Shallow copy of the current common characters so far
        # We will update the contents of this dictionary
        curr_chars = common_chars.copy()
        
        # Only update for characters already in curr_chars
        # We only care about the common characters, so don't
        # create new entries for newly encountered chars
        for char in curr_word:
            if char in curr_chars:
                curr_chars[char] -= 1
        
        for key, val in curr_chars.items():
            old_com = common_chars[key]
            
            # Exact same number of instances as common_chars, or more.
            # Keep the original common_chars entry
            if val <= 0:
                continue
            # No instances of the common char in this word; remove from
            # the common_char dictionary
            elif val == old_com:
                del common_chars[key]
            # Some non-zero number of instances of the char, but less than
            # the common_chars
            else:
                common_chars[key] = old_com - curr_chars[key]
    
    # Parse the common_chars dict into proper final format
    ans = []
    
    for key, val in common_chars.items():
        for _ in range(val):
            ans.append(key)
    
    return ans
