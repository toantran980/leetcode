import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''cnt = 0
        while n > 0:
            # check if the last bits is 1 using bitwise and
            if n & 1:
                cnt += 1
            # shift bits to the right by 1 (same as n // 2)
            n >>= 1
        return cnt'''

        cnt = 0
        while n:
            # remove the rightmost 1 bit
            n = n - 1 & n
            cnt += 1
        return cnt