class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:

            return []
        
        a = sorted(arr)

        res = []

        d1 = {}

        cnt = 1

        d1[a[0]] = cnt

        for i in range(1 , len(a)):

            if a[i] > a[i-1]:

                cnt +=1 

            d1[a[i]] = cnt

        print(d1)

        for i in arr:

            res.append(d1[i])

        return res