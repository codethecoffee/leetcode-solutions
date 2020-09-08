// Question: https://leetcode.com/problems/merge-intervals/
#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> merge(std::vector<std::vector<int>> &intervals) {
    int num_ints = intervals.size();

    if (num_ints == 0) {
      return {};
    }

    // Sort the intervals by increasing start time
    std::sort(intervals.begin(), intervals.end());

    // Initialize stack with the first interval
    std::vector<std::vector<int>> stack = {intervals[0]};

    for (int i = 1; i < num_ints; ++i) {
      std::vector<int> top_int = stack.back();
      std::vector<int> curr_int = intervals[i];

      // If there is an overlap, update the latest interval
      if (curr_int[0] <= top_int[1]) {
        if (curr_int[1] > top_int[1]) {
          stack.back()[1] = curr_int[1];
        }
      }
      // Otherwise, add curr_int as a new entry to the stack
      else {
        stack.push_back(curr_int);
      }
    }

    return stack;
  }
};