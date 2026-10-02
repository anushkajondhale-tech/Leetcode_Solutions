class Solution(object):
    def findTheDifference(self, s, t):
        total = 0

        for ch in t:
            total += ord(ch)

        for ch in s:
            total -= ord(ch)

        return chr(total)
                
        
        