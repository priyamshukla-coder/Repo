class Solution:
    def longestPalindrome(self, s: str) -> str:
        """"if len(s)==1:
            return s"""
        """s1=" "
        for i in range(len(s)):
            for j in range(len(s),i+1,-1):
                if len(s1)>=j-i:
                    break
                elif s[i:j]==s[i:j][::-1]:
                    s1=s[i:j]
                    break
        return s1
        """

        def recur(s , l , r):

            while l >= 0 and r < len(s) and s[l] == s[r]:

                l -= 1

                r += 1

            return s[l + 1 : r]

        res = []

        for i in range(len(s)):

            res .append(recur(s , i , i + 1))

            res.append(recur(s , i , i))

        return max(res , key = len)