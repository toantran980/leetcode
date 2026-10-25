class Solution:
    def isHappy(self, n: int) -> bool:
        # time complexity: O(logn)
        # space complexity: O(logn)
        # hashset approach
        v = set()

        while n not in v: 
            v.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False


        # fast-slow 2 point approach
        # same time complexity: O(log n)
        # better space complexity: O(1)
        '''slow, fast = n, self.sumOfSquares(n)
        power = som = 1

        while slow != fast:
            if power == som:
                slow = fast
                power *= 2
                som = 0  # reset digit
            fast = self.sumOfSquares(fast)
            som += 1
        if fast == 1:
            return True
        return False'''
    
    def sumOfSquares(self, n: int) -> int:
        output = 0 

        while n > 0:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
        return output


        