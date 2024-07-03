class Solution(object):
    def searchRange(self, nums, target):
        list1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                list1.append(i)
        
        if not list1:
            return [-1, -1]  
        else:
            return [list1[0], list1[-1]]  