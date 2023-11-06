class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_elements=Counter(nums)

        for i in count_elements:

            if count_elements[i]>len(nums)//2:

                return i
                
                        