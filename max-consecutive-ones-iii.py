class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        ans = 0     
        for right in range(n):
            if nums[right] == 0:
                zeros = zeros + 1              
            while zeros > k:
                if nums[left] == 0:
                    zeros = zeros - 1
                left = left + 1          
            current_len = right - left + 1
            if current_len > ans:
                ans = current_len            
        return ans
