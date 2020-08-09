# Link to problem: https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    s_len, t_len = len(s), len(t)
    # If strings are the same length, they must be identical
    if s_len == t_len:
        return s == t
    # If s is longer than t, it cannot be a subsequence
    elif s_len > t_len:
        return False
    
    # i: s index, j: t index
    i,j = 0,0
    
    while i < s_len and j < t_len:
        s_char, l_char = s[i], t[j]
        if s_char == l_char:
            i += 1
            j += 1
        else:
            j += 1
        
    return i >= s_len
