# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    # key: Number that adds up to target
    # value: Index the number is at
    two_sum = {}
    
    # Iterate through nums using indices b/c we need the indices
    # for the final ans
    for i in range(len(nums)):
        curr_num = nums[i]
        # Case 1: We found a pair that adds up to target
        if curr_num in two_sum:
            return [two_sum[curr_num], i]
        # Case 2: Add a new entry for the current number
        else:
            two_sum[target-curr_num] = i
    
    # If we go through the entire for loop without returning
    # there's no valid answer
    return -1