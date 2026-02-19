# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        # I need to traverse the lists and compare the values of the nodes
        # I need to return the head of the new sorted list
        # the head will be the smallest num
        # the lists are sorted already.

        curr_node1 = list1
        curr_node2 = list2
        head = 0
        while curr_node1:
            next_node1 = curr_node1.next
            next_node2 = curr_node2.next
            if curr_node2.val > curr_node1.val:
                curr_node1.next = curr_node2
            else: 
                curr_node2.next = curr_node1
            curr_node1 = next_node1
            curr_node2 = next_node2
        
        if list1.val > list2.val:
            head = list1
        else:
            head = list2

        return head
