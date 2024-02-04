# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def length(s1):
            
            st=0
            
            while s1:
                
                st=st+1
                
                s1=s1.next
                
            return st
        
        l=length(head)
        
        curr,prev=head,head
        
        if n==l:
            
            return curr.next
        
        if l==1:
            
            return ListNode(0).next
        
        st=0
        
        while st<(l-n):
            
            prev=curr
            
            curr=curr.next
            
            st=st+1
            
        prev.next=curr.next
        
        curr=prev
        
        return head