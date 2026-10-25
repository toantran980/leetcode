class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        maxL, maxR = 0, 0
        left = 0

        for right in range(len(nums)):
            currSum = max(currSum, 0)
            left = right

            currSum += nums[right]
            maxSum = max(currSum, maxSum)
            maxL, maxR = left, right

        return maxSum

        '''
        # First approach: brute force 
        # O(n^2)
        maxSum = nums[0]

        for i in range (len(nums)):
            currSum = 0
            for j in range (i, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        
        return maxSum
        

        # Better approach: O(n)
        # Initialize maxSum with the first element to handle arrays with all negative numbers
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            # If currSum becomes negative, it's better to start a new subarray 
            # from the current element 'n' rather than continuing to add to it.
            # almost same as expand windows (one kind of sliding windows)
            currSum = max(n, currSum + n)

            #or currSum = max(currSum, 0) + n
            
            # Keep track of the highest sum encountered
            maxSum = max(maxSum, currSum)

        return maxSum '''
