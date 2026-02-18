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
    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

# this traverses the list from the head to tail and reverses the pointers the nodes have to point to the head
        while curr:
            # save reference to the next node
            nxt = curr.next
            # point curr.next to previous node
            curr.next = prev
            # set previous node to current node
            prev = curr
            # set current node to nxt
            curr = nxt
        return prev



