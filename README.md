# Leetcode Solutions in Python and C++
[Click here](https://docs.google.com/spreadsheets/d/1EmRVQ2KEknTREwNd4-2qbSzScHMvgzDT0yGGT5u-yA8/edit?usp=sharing) for the google spreadsheet
organizing the questions by category and linked to the solution I wrote for each of them. This is always up to date with the README (with the power of a python script and GitHub workflows).

| Number | Question | Hints | Python Solution | C++ Solution |
|:------:|:--------:|-------|:---------------:|:------------:|
| 1 |[Two Sum](https://leetcode.com/problems/two-sum/) | Use a hash table to keep track of the indices of the numbers you've encountered so far. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0001_two_sum.py)  | [C++ Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/c%2B%2B_solutions/0001_two_sum.cpp) |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Implement both the iterative and recursive solution. What do we do if the linked list has an odd number of nodes? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0024_swap_nodes_in_pairs.py) | |
| 56 |[Merge Intervals](https://leetcode.com/problems/merge-intervals/)| Sort the intervals by increasing start time. |[Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0056_merge_intervals.py) | [C++ Solution](https://github.com/codethecoffee/leetcode-solutions/blob/8f2745c473c647ce3f7f8446c7e5215218106b50/c%2B%2B_solutions/0056_merge_intervals.cpp)|
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) |  Try iterating through each digit backwards. What do you do when the digit is a 9? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0066_plus_one.py)| |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Look at one element from each of the arrays, compare them, and make a decision depending on their relation to each other. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0088_merge_sorted_arrays.py)| |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Make sure you know how to implement this recursively. The iterative solution is a lot trickier. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/74ae6c933f170aa828fe2d9833a55ff98a3e6642/python_solutions/0094_binary_tree_inorder_traversal.py)| |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Keep track of the child nodes of ALL the nodes in the current level. That will be the next level you will traverse. Rinse and repeat until none of the nodes in the current level have children. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0122_best_time_to_buy_and_sell_stock_II.py) | |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/) | What should we do every time there is a valley followed by a peak in price? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0122_best_time_to_buy_and_sell_stock_II.py) | |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Try a recursive solution. Split the list up into the first node and the rest of the list. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0206_reverse_linked_list.py) | |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Maintain a hash set that keeps track of the numbers we've encountered so far. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0217_contains_duplicate.py) | [C++ Solution](https://github.com/codethecoffee/leetcode-solutions/blob/8f2745c473c647ce3f7f8446c7e5215218106b50/c%2B%2B_solutions/0217_contains_duplicate.cpp)|
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string) | Use the two pointer approach. Try implementing an iterative and recursive solution. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0344_reverse_string.py)| |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Use two pointers to iterate through the two strings simultaneously. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0392_is_subsequence.py)| |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Create a hash table keeping track of the number of occurrences of each character. How many of each can we include in our longest palindrome? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0409_longest_palindrome.py)| |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Sort the greed factors and cookies in decreasing (or increasing) order. What can we do with these sorted versions of the inputs? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0455_assign_cookies.py)| |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | How can be apply a modified version of the [merge intervals algorithm](https://leetcode.com/problems/merge-intervals/) to solve this question? | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0763_partition_labels.py)| |
| 771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0771_jewels_and_stones.py)| |
| 921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Keep track of the number of open "(" parens as you iterate through the sequence. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/0921_minimum_add_to_make_parentheses_valid.py)| |
| 1002 | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | Keep track of the common characters and their occurrences in a hash table. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/1002_find_common_characters.py)| |
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | Keep track of the numbers and their number of occurrences in a hash table. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/1207_unique_number_of_occurences.py)| |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | Create a max heap sorted by the number of occurrences of each number | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/1338_reduce_array_size_to_half.py)| |
| 1338 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Maintain a running sum in an array | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/1365_how_many_numbers_are_smaller_than_current_number.py)| |
| 1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Keep track of number of occurrences in a hash table. | [Python Solution](https://github.com/codethecoffee/leetcode-solutions/blob/master/python_solutions/1512_number_of_good_pairs.py)| |