class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low , high = 1 , max(piles)

        while low < high:

            mid = low+(high-low)//2

            curr = 0

            for i in piles:

                curr += ceil(i/mid)

            if curr <= h:

                high = mid

            else:

                low = mid+1

        return low