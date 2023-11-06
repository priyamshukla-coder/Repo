class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = 0

        mx = float("-inf")

        for i in range(len(nums)):

            # curr_max = max(nums[i] , curr_max + nums[i])

            curr_max = curr_max + nums[i]

            mx=max(mx , curr_max)

            if curr_max <= 0:

                curr_max = 0

        return mx

