# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = 0

        def maxDepth(root):
            nonlocal ans

            if not root: return -1
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            # 
            ans = max(ans, 2 + left + right)
            return 1 + max(left, right)
        
        maxDepth(root)
        return ans
        
