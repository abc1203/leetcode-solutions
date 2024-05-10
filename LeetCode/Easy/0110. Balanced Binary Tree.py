# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root: return True

        def height(root):
            if root: return 1 + max(height(root.left), height(root.right))
            return 0
        
        if self.isBalanced(root.left) and self.isBalanced(root.right) and \
        abs(height(root.left) - height(root.right)) <= 1:
            return True
        return False
        
