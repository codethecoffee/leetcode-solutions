# Link: https://leetcode.com/problems/swap-nodes-in-pairs/

######################
# ITERATIVE SOLUTION #
######################

class IterativeSolution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # EDGE CASE: Linked list has zero or one node
        if (head is None) or (head.next is None):
            return head

        left_node, right_node = head, head.next

        # Store the second node as the new head
        final_head = right_node

        while left_node and right_node:

            # Store reference to next left_node
            next_left = right_node.next
            if next_left:
                next_right = right_node.next.next
            else:
                next_right = None

            # Swap the left_node and right_node
            right_node.next = left_node
            left_node.next = next_right

            # If there is an odd number of nodes
            if (next_left) and (next_right is None):
                left_node.next = next_left
                break

            # Move onto the next pair of nodes
            left_node = next_left
            right_node = next_right

        return final_head


######################
# RECURSIVE SOLUTION #
######################
