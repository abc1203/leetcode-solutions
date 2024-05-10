# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root: return []

        ans = []
        ans.append([root.val])
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        for i in range(max(len(left), len(right))):
            if i < min(len(left), len(right)):
                ans.append(left[i] + right[i])
            elif i >= len(left):
                ans.append(right[i])
            elif i >= len(right):
                ans.append(left[i])

        return ans
        
