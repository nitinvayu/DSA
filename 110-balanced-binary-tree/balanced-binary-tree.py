# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = False

    def depth(self, root):
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left - right) > 1:
            self.ans = False
        return (left if left > right else right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.depth(root)
        return self.ans
        