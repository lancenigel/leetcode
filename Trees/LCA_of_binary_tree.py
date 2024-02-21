# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        curr = root

        while curr:
            if p.val > cur.val and q.val > cur.val:
                curr = cur.right
            elif p.val < cur.val and q.val < cur.val:
                curr = cur.left
            else:
                return cur
