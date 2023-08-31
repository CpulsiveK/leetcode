class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_len = len(nums)
        nums_exists = {}

        for i in range(nums_len):
            difference = target - nums[i]

            if difference in nums_exists:
                return [nums_exists[difference], i]
            else:
                nums_exists[nums[i]] = i