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


        dummy = ListNode()
# we name this pointer tail as its "tailing" where we are at in the lists
        tail = dummy
# check if both lists are not empty
        while list1 and list2:
# whichever is smaller, thats the next node
# progress the nodes on the list that was smaller
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
# so basically we progress one of the lists at a time depending on which list.val is less than the other
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

# exhust each list if not exhausted
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
# dummy is a blank node it has no value, the next node is our "head"
# "give me everything after that placeholder node from the start"
        return dummy.next
