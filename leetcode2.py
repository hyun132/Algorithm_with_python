# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = l1
        prev = node = None
        c=0
        while l1:
            if l2 is None and c<1:
                break
            sum = c + l1.val 
            if l2:
                sum+= l2.val
            
            l1.val = sum % 10
            c= sum // 10
            
            # l2가 더 길 때 l1에 이어붙여주기
            if l2:
                if l2.next and l1.next is None:
                    l1.next = l2.next
                    l2.next=None
            prev = l1
            
            #다음 노드로 이동
            l1=l1.next
            if l2:
                l2=l2.next
         
        #l1이 끝났는데 자리올림수가 있으면
        if c>0:
            prev.next = ListNode(c)

        
        return root
