# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
#
# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]
#
# Example 2:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time complexity 0(1) space because of additional pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# node1 -> node2 -> node3 
# return new head after reversing

# iterate through nodes, while iterating, swapping pointers, the end is my new head
# two pointer solution
        curr_node, prev_node = head, None
        while curr_node:
# first thing, create temp pointer to next node
# because we need to know where we are going, its where curr node will be next iteration

            next_node = curr_node.next
# the whole point is to change the pointers in the other direction
# point curr_node to where its from - previous node
            curr_node.next = prev_node
            # set prev = curr
# we need to progress prev node so that current node when it progresses can point back to previous node
            prev_node = curr_node
            # move cur to next
            curr_node = next_node
#prev node will be pointing at the head because cur_node will be null when it reaches there.
        return prev_node

