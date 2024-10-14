class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap =[]

        for i in nums:

            heapq.heappush(heap , -1 * i)

        score = 0

        while k != 0:

            val = -1*heapq.heappop(heap)

            score += val

            heapq.heappush(heap , -1 * (math.ceil(val/3)))

            k -= 1

        return score