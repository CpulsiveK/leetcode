class Solution(object):
    # recursive solution 
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        try:
            if len(nums) == 0:
                return
            
            nums.remove(val)

            if val in nums:
                self.removeElement(nums, val)
            else:
                print(nums)
                return len(nums)
        except ValueError as err:
            print(err)

    # non recursive solution 
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        try:
            if len(nums) == 0:
                return
            
            while val in nums:
                nums.remove(val)
            
        except ValueError as err:
            print(err)