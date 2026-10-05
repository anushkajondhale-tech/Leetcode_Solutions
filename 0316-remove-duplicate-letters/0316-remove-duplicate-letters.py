class Solution(object):
    def removeDuplicateLetters(self, s):
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        result = []

        for i in range(len(s)):
            if s[i] in result:
                continue

            while result and result[-1] > s[i] and last[result[-1]] > i:
                result.pop()

            result.append(s[i])

        return "".join(result)

        