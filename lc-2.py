# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        h = r = ListNode("head")
        s = 0
        while l1 or l2:
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            r.next = ListNode(s%10)
            s=s/10
            r = r.next
        if s == 1:
            r.next = ListNode(1)
        return h.next
