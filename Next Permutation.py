class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums == sorted(nums,reverse=True):

           nums.reverse()

           return

        st = len(nums) - 2

        while st>=0 and nums[st]>=nums[st+1]:

            st -= 1

        end = len(nums) - 1

        while end >=0 and nums[st]>=nums[end]:

            end -= 1

        nums[st] , nums[end] = nums[end] ,nums[st]

        nums[st+1:] = reversed(nums[st+1:])

