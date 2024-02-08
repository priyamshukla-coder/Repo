class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(fst = 0 , curr = []):

            if len(curr) == i:

                res.append(curr[:])

                return 

            for idx in range(fst , len(nums)):

                curr.append(nums[idx])

                backtrack(idx+1 , curr)

                curr.pop()

        res = []

        for i in range(0,len(nums)+1):

            backtrack()

        return res
        