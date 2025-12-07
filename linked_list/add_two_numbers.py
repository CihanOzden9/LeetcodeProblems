

class ListNode:
    def __init__(self,val, next=None):
        self.val = val
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode() #sonuç listesi
        curr = result #liste takibi
        carry = 0 # Ondalıklardan fazlasını taşımak için taşıyıcı
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return result.next
"""
l1 = [2,4,3]

l2 = [5,6,4]
-----
sonuç = [7,0,8]

"""