class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last_merge_index = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_merge_index] = nums1[m - 1] 
                m -= 1
            else:
                nums1[last_merge_index] = nums2[n - 1]
                n -= 1
            last_merge_index -= 1

        while n > 0:
            nums1[last_merge_index] = nums2[n - 1]
            n, last_merge_index = n - 1, last_merge_index - 1

solution = Solution()
print(solution.merge([0], 0, [1], 1))
