class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1, n2 = len(word1), len(word2)
        for i in range(min(n1, n2)):
            res.append(word1[i])
            res.append(word2[i])       
        res.append(word1[i+1:])
        res.append(word2[i+1:])       
        return "".join(res)
