class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        # Time complexity: O(n), Space Complexity: O(n)
        s1 = []
        for ch in s:
            if ch.isalnum():
                s1.append(ch.lower())

        s1 = ''.join(s1)
        rev = s

        return s1 == rev
        '''

        # Time complexity: O(n), Space complexity: O(1)
        i = 0
        j =  len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True
