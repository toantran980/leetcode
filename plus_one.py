class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]'''


        n = len(digits) 
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


        
