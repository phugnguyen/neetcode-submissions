# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3 pointers, prev, current, temp to hold next node
        # iterate through until we reach the end (.next is None)
        # return new head
        prev = None
        current = head

        # None <- [] <- [] <- [p] c = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev