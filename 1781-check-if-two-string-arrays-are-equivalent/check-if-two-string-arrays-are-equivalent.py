class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        for word in word1:
            res1=''.join(word1)
        for word in word2:
            res2=''.join(word2)
        if res1==res2:
            return True
        else:
            return False
        