# Merge the two lists into one sorted list. The list should be made 
# by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l1
        if not l2: return l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)