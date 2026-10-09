class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1 = ""
        str2 = ""

        while l1:
            str1 += str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        total = str(int(str1) + int(str2))

        dummy = ListNode(0)
        current = dummy

        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next