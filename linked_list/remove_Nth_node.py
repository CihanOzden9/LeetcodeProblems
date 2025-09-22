
class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthNode(self, head, n):
        left_pointer = head
        right_pointer = head
        
        while n > 0 and right_pointer:
            right_pointer = right_pointer.next
            n -= 1
        
        while right_pointer and right_pointer.next:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
            
        if left_pointer == head and not right_pointer:
            return head.next
        left_pointer.next = left_pointer.next.next
        return head