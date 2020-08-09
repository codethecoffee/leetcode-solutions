# Link to problem: https://leetcode.com/problems/reverse-string/

# ITERATIVE SOLUTION
# Time complexity: O(n), Space complexity: O(1)
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    str_len = len(s)
    
    if str_len in {0,1}:
        return s
    
    # Initialize two "pointers"; one at the first char, one at the last char
    l,r = 0, str_len-1
    
    # Swap the characters at the ends of the current substring
    # until l and r completely converge in the middle
    while l < r:
        old_l, old_r = s[l], s[r]
        s[l], s[r] = old_r, old_l
        l+=1
        r-=1


# RECURSIVE SOLUTION
# Time complexity: O(n), Space complexity: O(n) because of the stack space

def reverseHelper(s, l, r):
    """
    Recursive helper function to do the work for reversing the string s
    """
    # Base case: l and r have converged
    if l >= r:
        return
    
    # Swap the two characters in place
    old_l, old_r = s[l], s[r]
    s[l], s[r] = old_r, old_l
    
    # In recursive call, increment l and decrement r
    # so that they inch closer to the middle of string
    reverseHelper(s, l+1, r-1)

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    str_len = len(s)
    l, r = 0, str_len-1
    
    reverseHelper(s, l, r)