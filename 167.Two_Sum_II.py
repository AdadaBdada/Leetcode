# 167. Two Sum II - Input array is sorted


class Solution:

    # Dictionary
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = {}
        for index, value in enumerate(numbers):
            diff = target - value
            if diff in res:
                return [res[diff], index+1]
            res[value] = index+1

    # Two Pointer Solution
    def twoSum2(self, numbers, target):

        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":

    # Dictionary 0.312s
    # Two Pointer 0.262s

    numbers = [2, 7, 11, 15]
    target = 9
    s = Solution()
    res = s.twoSum2(numbers, target)
    print(res)
