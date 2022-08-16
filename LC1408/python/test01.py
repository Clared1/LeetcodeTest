class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x))
        tmpans = set()
        ans = []
        while(words):
            tmp = words.pop()
            for i in tmpans:
                if tmp in i:
                    ans.append(tmp)
                    break
            else:
                tmpans.add(tmp)
        return ans