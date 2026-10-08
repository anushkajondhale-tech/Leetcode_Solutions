class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        count = 0
        i = 0

        while i < len(s):
            if s[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 1 and s[i] == "(":
                del s[i]
                continue

            if count == 0 and s[i] == ")":
                del s[i]
                i -= 1

            i += 1

        return "".join(s)