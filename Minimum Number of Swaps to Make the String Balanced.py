class Solution:
    def minSwaps(self, s: str) -> int:
        
        q1 = deque()

        cnt = 0

        for i in s:

            if i == '[':

                q1.append(i)

            else:

                if len(q1) > 0:

                    q1.pop()

                else:

                    cnt += 1

        return (cnt  + 1) // 2