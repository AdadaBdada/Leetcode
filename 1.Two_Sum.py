class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in res:
                return [res[diff], index]
            res[value] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    res = s.twoSum(nums, target)
    print(res)

    # edge case nums = [3,3] target = 6 | nums = [3,2,4] target = 6
