class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # T.C. : O(N)

        # S.C. : O(1)

        # Boyer-Moore Voting Algorithm 

        cnt1 , cnt2 , ele1 ,ele2 =0 ,0  , float("-inf") , float("-inf")

        for i in range(len(nums)):

            if cnt1 == 0 and nums[i] != ele2:

                cnt1=1

                ele1=nums[i]

            elif cnt2 == 0 and nums[i] != ele1:

                cnt2=1

                ele2=nums[i]

            elif ele1 == nums[i]:

                cnt1=cnt1+1

            elif ele2 == nums[i]:

                cnt2=cnt2+1

            else:

                cnt1=cnt1-1

                cnt2=cnt2-1

        cnt11 , cnt22 = 0 , 0

        res=[]

        for i in range(len(nums)):

            if nums[i] == ele1:

                cnt11+=1

            if nums[i] == ele2:

                cnt22+=1

        limit = int(len(nums)/3)+1

        if cnt11>=limit:

            res.append(ele1)

        if cnt22>=limit:

            res.append(ele2)

        res.sort()

        return res

        