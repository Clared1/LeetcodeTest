class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        index = sorted(set(arr))
        arrtoindex = {p:(i+1) for i, p in enumerate(index)}
        return [arrtoindex[i] for i in arr]