class Solution(object):
    def searchInsert(self, nums, target):
        # define left and right pointers
        l = 0
        r = len(nums) - 1
        # write binary search algorithm to find target in logn time
        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else: 
                return mid
            
        return l
