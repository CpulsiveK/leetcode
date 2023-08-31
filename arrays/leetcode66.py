class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str_digits = []

        for i in digits:
            str_digits.append(str(i))

        num = int("".join(str_digits)) + 1
        str_digits = list(str(num))
        digits = []

        for i in str_digits:
            digits.append(int(i))
        
        return digits