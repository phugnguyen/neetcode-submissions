# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find nth node by sending a fast pointer n nodes ahead of the slow pointer
        
        # have a temp node node follow the the slow pointer to do the deletion
        temp = ListNode(0, head)
        left = temp
        right = head

        # increment right n times ahead
        while n > 0:
            right = right.next
            n -= 1

        # then increment both until faster pointer is at the end
        while right:
            left = left.next
            right = right.next

        
        # delete
        left.next = left.next.next

        # return head
        return temp.next
