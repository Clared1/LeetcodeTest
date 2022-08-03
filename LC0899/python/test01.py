class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return  ''.join(sorted([i for i in s]))
        else:
            tmp = s+s
            tmpans = s
            for i in range(len(s)):
                tmpans = min(tmpans, tmp[i:i+len(s)])
            return tmpans


