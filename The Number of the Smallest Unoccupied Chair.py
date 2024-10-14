class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        val = times[targetFriend]

        times.sort()

        time = [0] * len(times)

        for i in times:

            for j in range(len(times)):

                if time[j] <= i[0]:

                    time[j] = i[1]

                    if i == val:

                        return j

                    break

        return 0 