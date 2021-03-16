#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Date:16/03/2021
148. Sort List - Leetcode Medium

We will use Merge Sort to solve the problem
"""
class Solution:
    
    def merge(self,left_List,right_List):
        head = ListNode()
        current = head
        while(left_List and right_List):
            if left_List.val<right_List.val:
                current.next = left_List
                left_List = left_List.next
            else:
                current.next = right_List
                right_List = right_List.next
            current=current.next
        
        if left_List:
            current.next = left_List
            current = current.next
        if right_List:
            current.next = right_List
            current = current.next
        
        return head.next
    
    
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next == None:
            return head
        temp=head
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            temp=slow
            slow=slow.next
            fast=fast.next.next
                
        temp.next=None
        left_List = self.sortList(head)
        right_List = self.sortList(slow)
        
        return self.merge(left_List,right_List)
        
        
    
        
        
        