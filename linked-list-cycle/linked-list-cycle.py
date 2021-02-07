# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #have 2 pointers, slow and fast, moving at different speeds.
        #the fast pointer moves at twice the speed as slow pointer.
        #if fast pointer ever equals the slow pointer, then that means
        #that the fast pointer had to make a cycle to reach the slow pointers'
        #position. Therefore, implying a cycle in the linkedList.
        slow = fast = head
        if head is None:
            return False
        
        while fast is not None:
            fast = fast.next.next if fast.next is not None else None
            if(slow == fast):
                return True
            slow = slow.next

        return False
            