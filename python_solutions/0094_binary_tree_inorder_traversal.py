# Question: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

########################
## RECURSIVE SOLUTION ##
########################

class Solution:
    def inorderHelper(self, curr_node, traversal):
        if curr_node is None:
            return
        
        self.inorderHelper(curr_node.left, traversal)
        traversal.append(curr_node.val)
        self.inorderHelper(curr_node.right, traversal)
    
    def inorderTraversal(self, root: TreeNode):
        traversal = []
        self.inorderHelper(root, traversal)
        return traversal
