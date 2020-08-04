# Link: https://leetcode.com/problems/partition-labels/

def partitionLabels(S):
    num_chars = len(S)
    char_ranges = {}
    
    for i in range(num_chars):
        curr_char = S[i]
        # Update index for last occurrence of curr_char
        if curr_char in char_ranges:
            char_ranges[curr_char][1] = i
        # curr_char occurred once so far, so start == end index
        else:
            char_ranges[curr_char] = [i,i]
    
    ranges = []
    for val in char_ranges.values():
        ranges.append(val)
    
    # Sort the ranges in order of increasing index
    ranges.sort()
    
    # Initialize stack with the first range
    stack = [ranges[0]]
    
    for i in range(1, len(ranges)):
        top = stack.pop()
        curr = ranges[i]
        
        # Case 1: There's overlap between top and curr
        if curr[0] <= top[1]:
            new_interval = [top[0], max(top[1], curr[1])]
            stack.append(new_interval)
        # Case 2: No overlap, start a new interval
        else:
            stack.extend([top, curr])
    
    ans = []
    
    # Calculate the length of each partition
    for partition in stack:
        ans.append((partition[1]-partition[0])+1)
    
    return ans