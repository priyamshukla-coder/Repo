# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root , p , q):

            if root is None:

                return None

            if root.val == p.val or q.val == root.val:

                return root

            left , right = lca(root.left , p , q), lca(root.right , p , q)

            if left is not None and right is not None:

                return root
                
            return left if left is not None else right

        return lca(root,p,q)
        