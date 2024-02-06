"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copyMap = {None: None}

        cur = head

        while cur:
            copy = ListNode(cur.val)
            copyMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copyMap[cur]
            copy.next = copyMap[cur.next]
            copy.random = copyMap[cur.random]

            cur = cur.next

        return copyMap[head]
