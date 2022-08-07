from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpdict = dict()
        for i, p in enumerate(nums):
            if target-p in tmpdict:
                return [i, tmpdict[target-p]]
            else:
                tmpdict[p] = i