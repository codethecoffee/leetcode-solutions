# Link to problem: https://leetcode.com/problems/assign-cookies/

def findContentChildren(g, s):
    # Sort the children and the cookies in increasing order
    g.sort() # Children greed factors
    s.sort() # Cookie sizes
    
    content = 0 # Number of content children
    i,j = 0,0 # i: index in g, j: index in s
    num_child, num_cook = len(g), len(s)
    
    while i < num_child and j < num_cook:
        curr_child = g[i]
        curr_cook = s[j]
        # Current child content with the current cookie
        if curr_child <= curr_cook:
            content += 1
            i += 1
            j += 1
        else:
            # Current child too greedy to be content w/ current cookie
            j += 1 # Try out a larger cookie
            
    return content
