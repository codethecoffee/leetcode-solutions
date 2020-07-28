# Link to problem: https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    num_count = {}
    for n in nums:
        if n not in num_count:
            num_count[n] = 1
        else:
            num_count[n] += 1
    
    good_pairs = 0
    
    for count in num_count.values():
        good_pairs += (count*(count-1))//2
    
    return good_pairs
    