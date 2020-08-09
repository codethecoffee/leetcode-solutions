# Link: https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    # A set keeping track of the numbers encountered so far
    num_seen = set()
    
    for curr_num in nums:
        # Case 1: We have seen curr_num earlier on in nums
        if curr_num in num_seen:
            return True
        # Case 2: First encounter with curr_num
        else:
            num_seen.add(curr_num)
    
    # If we go through the entire for loop without returning
    # there are no duplicates
    return False