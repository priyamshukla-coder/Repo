class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        cnt_bits = 0

        while left != right:
            
            cnt_bits += 1 

            left = left >> 1

            right = right >> 1

        print(left , right)

        return left << cnt_bits
        