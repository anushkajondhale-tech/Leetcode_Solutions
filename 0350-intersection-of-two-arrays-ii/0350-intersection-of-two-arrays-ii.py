class Solution:
    def intersect(self, nums1, nums2):
        result = []

        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)

        return result

        