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

        if len(preorder) == 0: return None
        root, n = preorder[0], len(preorder)
        i = 0
        while i < n and inorder[i] != root:
            i += 1
        left_inorder, right_inorder = inorder[:i], inorder[i+1:]
        left_preorder, right_preorder = preorder[1:i+1], preorder[i+1:]
        
        left_subtree = self.buildTree(left_preorder, left_inorder)
        right_subtree = self.buildTree(right_preorder, right_inorder)
        root_node = TreeNode(val=root, left=left_subtree, right=right_subtree)

        return root_node
        


        





        
