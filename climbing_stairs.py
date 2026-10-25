class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1  # ways to reach step i-1 and i-2

        for i in range(n - 1):
            one, two = one + two, one

        return one
        