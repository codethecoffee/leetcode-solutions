// Question: https://leetcode.com/problems/contains-duplicate/
#include <unordered_set>
#include <vector>

class Solution
{
public:
    bool containsDuplicate(std::vector<int> &nums)
    {
        int num_ints = nums.size();
        std::unordered_set<int> unique_nums{};

        for (int i = 0; i < num_ints; i++)
        {
            int curr_int = nums[i];

            // Case 1: curr_int not encountered yet
            if (unique_nums.find(curr_int) == unique_nums.end())
            {
                unique_nums.insert(curr_int);
            }
            // Case 2: curr_int is a duplicate
            else
            {
                return true;
            }
        }

        return false;
    }
};