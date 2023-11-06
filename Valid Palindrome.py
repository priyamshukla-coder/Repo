class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()

        s1=""

        for i in s:

            if i.isalpha() or i.isdigit():

                s1=s1+i

        return True if s1==s1[::-1] else False