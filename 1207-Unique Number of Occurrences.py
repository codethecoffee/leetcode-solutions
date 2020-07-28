# Link to question: https://leetcode.com/problems/unique-number-of-occurrences/

def uniqueOccurrences(arr):
    num_count = {}
    
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    unique_occ = set()
    for num, occ in num_count.items():
        if occ in unique_occ:
            return False
        else:
            unique_occ.add(occ)
    
    return True

print("Hello")
