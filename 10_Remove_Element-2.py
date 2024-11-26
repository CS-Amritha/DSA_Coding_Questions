class Solution(object):
    def removeElement(self, nums, val):
        nums2 = []  

        for num in nums:
            if num != val: 
                nums2.append(num)  

        count = len(nums2)  
        return count, nums2
