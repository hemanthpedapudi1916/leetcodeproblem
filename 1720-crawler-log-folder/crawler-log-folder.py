class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0
        for word in logs:
            if word[0].isalpha() or word[0]=='1':
                count += 1
            elif word == '../' and count > 0:
                count -= 1
        return count
        