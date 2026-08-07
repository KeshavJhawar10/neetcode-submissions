# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque([(root,float('-inf'))])
        good_nodes = 0

        while q:
            qLen = len(q)
            for _ in range(qLen):
                node, curr_max = q.popleft()
                if node:
                    if node.val >= curr_max:
                        good_nodes +=1
                        curr_max = node.val
                    q.append((node.left, curr_max))
                    q.append((node.right, curr_max))
        return good_nodes