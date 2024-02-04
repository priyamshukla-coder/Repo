class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        cnt = 0
        
        curr = 0
        
        for i in range(0,len(nums)):
            
            curr = curr+nums[i]
            
            if curr == 0 :
                
                cnt += 1
                
        return cnt