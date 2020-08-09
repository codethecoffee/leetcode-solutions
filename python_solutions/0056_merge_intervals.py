# https://leetcode.com/problems/merge-intervals/
def merge(intervals):
    num_intervals = len(intervals)
    
    # Sort intervals by increasing start time
    intervals.sort()
    
    if num_intervals in {0, 1}:
        return intervals
    
    # Initialize stack with the first interval
    stack = [intervals[0]]
    
    for i in range(1, num_intervals):
        top = stack.pop()
        curr_int = intervals[i]
        
        # If there is an overlap, merge top and curr_int
        # and add the new interval to the stack
        if curr_int[0] <= top[1]:
            merged = [top[0], max(curr_int[1], top[1])]
            stack.append(merged)
        # If the current interval doesn't overlap at all
        else:
            stack.extend([top, curr_int])
    
    return stack