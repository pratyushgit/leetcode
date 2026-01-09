# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_linkedlist(head):
    curr = head
    prev = None
    while curr.next:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr.next = prev
    prev = curr
    return prev

def display_ll(head) -> list:
    current = head
    out = []
    while current:
        out.append(current.val)
        current = current.next
    print(out)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        print("### input l1")
        display_ll(l1)
        print("### input l2")
        display_ll(l2)
        l1_reverse = reverse_linkedlist(l1)
        l2_reverse = reverse_linkedlist(l2)
        print("### output l1")
        display_ll(l1_reverse)
        print("### output l2")
        display_ll(l2_reverse)


## Test Case 1
ll1_n1 = ListNode(2)
ll1_n2 = ListNode(4)
ll1_n3 = ListNode(3)
ll1_n1.next = ll1_n2
ll1_n2.next = ll1_n3
ll1_head = ll1_n1
ll2_n1 = ListNode(5)
ll2_n2 = ListNode(6)
ll2_n3 = ListNode(4)
ll2_n1.next = ll2_n2
ll2_n2.next = ll2_n3
ll2_head = ll2_n1
Solution().addTwoNumbers(ll1_head,ll2_head)



