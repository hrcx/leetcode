# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum=0
        res=pre=ListNode(0)
        while l1 or l2 or sum:
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next

            sum,val=divmod(sum,10)
            pre.next=pre=ListNode(val)
        return res.next

