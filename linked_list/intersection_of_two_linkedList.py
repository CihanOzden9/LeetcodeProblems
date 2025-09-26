# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA,headB):
        first = headA
        second = headB

        while first != second:
            first = first.next if first != None else headB
            second = second.next if second != None else headA
        return first
            