# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # T.C. : O(Nlogn)

        # S.C. : O(N)

        def level_traversal(root):

            q1=deque([])

            mp=defaultdict(list)

            q1.append([root,0])

            while len(q1)>0:

                node , vertical = q1.popleft()

                if node is not None :

                    mp[vertical].append(node.val)

                    q1.append([node.left , vertical-1])

                    q1.append([node.right , vertical+1])

            print(mp)

            # mp.sort(mp.keys())

            res= []

            for i in  sorted(mp.keys()):

                res.append(mp[i])

            return res

        return level_traversal(root)
        