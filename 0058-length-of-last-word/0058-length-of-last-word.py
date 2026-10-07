class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        last=l[-1]
        if(len(last)==0):
            last_ele=l[-2]
            return len(last_ele)
        else:
            return len(last)

       
        