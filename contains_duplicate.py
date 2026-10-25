class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in nums:
            if i in dup:
                return True
            dup.add(i)
        return False

        '''dup = {}
        for i in nums:
            if i  in dup:
                return True
            else:
                dup[i] = 0
        return False'''
            
        