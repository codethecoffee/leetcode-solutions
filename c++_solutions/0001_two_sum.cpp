#include <stdio.h>
#include <utility>
#include <unordered_map>
#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // key: target - encountered num, value: index of encountered num
        std::unordered_map<int, int> num_pos;
        int num_items = nums.size();
        
        for (int i=0; i < num_items; i++) {
            int curr_num = nums[i];
            // If the current number is not in the map
            if (num_pos.count(curr_num) == 0) {
                int sec_num = target-curr_num;
                num_pos.insert(std::make_pair(sec_num, i));
            } 
            // If the current number is in the map, you found the answer
            else {
                return {num_pos[curr_num], i};
            }
        }
        
        // If we go through the entire for loop without returning the answer
        // it means there was no valid pair
        return std::vector<int>();
    }
};