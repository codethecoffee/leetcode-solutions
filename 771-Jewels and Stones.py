# Link to problem: https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(self, J: str, S: str) -> int:
    num_jewels = 0
    
    for char in S:
        if char in J:
            num_jewels += 1
    
    return num_jewels
