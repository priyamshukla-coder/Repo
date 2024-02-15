# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root):

            res = []

            if root is None:

                return res

            q1 = deque([])

            q1.append(root)

            while q1:

                l = len(q1)

                curr = []

                for i in range(l):

                    node = q1.popleft()

                    curr.append(node.val)

                    if node.left:

                        q1.append(node.left)

                    if node.right:

                        q1.append(node.right)

                print(curr)

                    
                res.append(curr)

            return res

        return bfs(root)
        