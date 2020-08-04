# Link: https://leetcode.com/problems/reduce-array-size-to-the-half/

import heapq

def minSetSize(arr):
    half_len = len(arr)//2
    # Hash table to keep track of the number of occurrences
    num_count = {}
    
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Initialize an empty max heap sorted by decreasing order of
    # occurences. Make the count negative to achieve this effect
    # since heapq only provides implementation for a min heap
    max_heap = []
    for num, count in num_count.items():
        curr_pair = [-count, num]
        heapq.heappush(max_heap, curr_pair)
            
    # The number of integers that we removed so far
    num_removed = 0
    num_elements = 0
    while num_removed < half_len and len(max_heap) > 0:
        # Current number with the greatest number of occurrences
        curr_max = heapq.heappop(max_heap)
        # Turn the count back to positive value and add them
        num_removed += -(curr_max[0])
        num_elements += 1
    
    return num_elements