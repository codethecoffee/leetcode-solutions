# Question: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []

        curr_nodes = [root]  # Nodes in the current level of the tree

        traversal = []  # The final answer to return

        while len(curr_nodes) > 0:
            next_nodes, curr_level = [], []

            # For each node in the current level of the tree...
            for node in curr_nodes:
                # If a left child exists
                if node.left:
                    next_nodes.append(node.left)
                # If a right child exists
                if node.right:
                    next_nodes.append(node.right)

                curr_level.append(node.val)

            # Set the next level of nodes to traverse through
            curr_nodes = next_nodes

            # Add values of the current level to the final answer
            traversal.append(curr_level)

        return traversal
