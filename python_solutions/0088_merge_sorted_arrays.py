# https://leetcode.com/problems/merge-sorted-array/

def merge(nums1, m, nums2, n):
    # Iterate through both of the sorted arrays at the same time
    while m > 0 and n > 0:
        curr_1 = nums1[m-1]
        curr_2 = nums2[n-1]

        if curr_1 >= curr_2:
            nums1[(m+n)-1] = curr_1
            m -= 1
        else: # curr_2 > curr_1
            nums1[(m+n)-1] = curr_2
            n -= 1
    
    # If there are smaller elements left in nums2, copy them over.
    # No need to do this for leftover num1 elements, since we're
    # merging into nums1 and the elements will already be there.
    while n > 0:
        nums1[n-1] = nums2[n-1]
        n -= 1
    
    return nums1