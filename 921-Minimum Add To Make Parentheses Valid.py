# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

def minAddToMakeValid(S):
    # Number of parens to add 
    num_add = 0
    
    # Number of open parens so far
    num_open = 0
    
    for char in S:
        # Current paren is an open paren
        if char == "(":
            num_open += 1
        # Curren paren is closed, and there's a match
        elif num_open > 0:
            num_open -= 1
        # No open paren for valid match
        else:
            num_add += 1
    
    # If there are open parens that aren't closed yet
    # you must add an equal number of closing parens
    if num_open > 0:
        num_add += num_open
    
    return num_add