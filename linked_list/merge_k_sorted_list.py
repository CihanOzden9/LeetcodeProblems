# Definition for singly-linked list.
"""
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        
        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next
        if not nums:
            return None
        
        nums.sort()

        dummy = ListNode(0)
        curr = dummy

        for node in nums:
            curr.next = ListNode(node)
            curr = curr.next

        return dummy.next




example = [[1,4,5],[1,3,4],[2,6]]

Solution().mergeKLists(example)