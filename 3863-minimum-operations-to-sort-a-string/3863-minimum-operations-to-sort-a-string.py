class Solution:
    def minOperations(self, s):
        n = len(s)
        mn = min(s)
        mx = max(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        if s[0] == mn or s[-1] == mx:
            return 1

        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3