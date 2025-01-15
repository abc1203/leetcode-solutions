# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]

        preorder => root -> left -> right
        inorder => left -> root -> right

         - preorder has root first, so iterate inorder until we found root
         - so we know what nodes are left & right; do it repeatedly
        """

        hm = {}

        for i in range(len(inorder)):
            hm[inorder[i]] = i
        
        preorder = collections.deque(preorder)

        def buildSubTree(start, end):
            if start > end: return None

            root = TreeNode(val=preorder.popleft())
            m = hm[root.val]

            root.left = buildSubTree(start, m - 1)
            root.right = buildSubTree(m + 1, end)
            return root
            
        return buildSubTree(0, len(preorder) - 1)
        


        





        
