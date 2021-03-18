
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
"""
Date:16/03/2021
21. Merge Two Sorted Lists - Leetcode Easy

The following is simple linked list problem
"""
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        current=head
        while(l1 and l2):
            if l1.val<l2.val:
                current.next = l1
                l1=l1.next
            else:
                current.next = l2
                l2=l2.next
            current = current.next
        if l1:
            current.next =l1
        
        if l2:
            current.next = l2
        return head.next
        