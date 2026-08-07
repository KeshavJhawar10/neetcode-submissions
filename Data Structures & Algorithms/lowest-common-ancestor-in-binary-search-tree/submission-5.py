# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        self.helper(root, p, q)
        return self.res

    def helper(self, root, p, q):
        if not root:
            return
        if self.isDescendent(root, p) and self.isDescendent(root, q):
            self.res = root
        self.helper(root.left, p, q)
        self.helper(root.right, p, q)

    def isDescendent(self, root, node):
        if not root:
            return False
        if root.val == node.val:
            return True
        return self.isDescendent(root.left, node) or self.isDescendent(root.right, node)
