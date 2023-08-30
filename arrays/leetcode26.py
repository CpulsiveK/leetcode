class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
                k += 1
                
        return k
                  
            
solution = Solution()
res = solution.removeDuplicates([1,1,2,2,3,3,4,4,5,6])
print(res)