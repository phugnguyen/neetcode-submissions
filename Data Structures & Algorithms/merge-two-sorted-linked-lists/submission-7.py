# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        curr = result = ListNode(0, None)

        while p1 and p2:
            if p1.val >= p2.val:
                curr.next = p2
                p2 = p2.next
            else:
                curr.next = p1
                p1 = p1.next
            if curr.next:
                curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2

        return result.next


