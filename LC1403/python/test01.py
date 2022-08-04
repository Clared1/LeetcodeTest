from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        tmpsum = sum(nums)
        nums.sort()
        ans = []
        tmpans = 0
        while(nums):
            tmp = nums.pop()
            tmpans+=tmp
            ans.append(tmp)
            if 2*tmpans > tmpsum:
                break
        return ans
