# Link to question: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
def smallerNumbersThanCurrent(nums):
    count = [0]*101
    
    for num in nums:
        count[num] += 1
    
    # Maintain a running sum in the count array
    for i in range(1, 101):
        count[i] += count[i-1]
            
    final_ans = [0] * len(nums)
    
    # Format to fit output answer
    for i in range(len(nums)):
        curr_num = nums[i]
        # If the number is 0, there will never be elements less than it
        if curr_num == 0:
            final_ans[i] = 0
        else:
        # Set it to the running sum up to the previous element in nums
            final_ans[i] = count[curr_num-1]
    
    return final_ans