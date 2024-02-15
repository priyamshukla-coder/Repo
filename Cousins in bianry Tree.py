# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # T.C. : O(N)

        # S.C. : O(h) depends on depth of recursion

        def traverse(root , parent , x , y , height):

            if root is None:

                return 

            if root.val == x:

                self.xparent = parent

                self.xheight = height

            elif root.val == y:

                self.yparent = parent

                self.yheight = height

            else:

                traverse(root.left , root , x , y , height+1)

                traverse(root.right , root , x , y , height+1)

        if root.val == x or root.val == y :

            return False

        self.xparent , self.yparent = -1 , -1

        # xparent = -1

        self.xheight , self.yheight = -1 , -1

        # yparent = -1

        traverse(root , None ,x ,  y , 0)

        # print(xheight , xparent , yheight , yparent)

        if self.xparent != self.yparent and self.xheight == self.yheight:

            return True

        return False


        