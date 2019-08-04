# 266. Palindrome Permutation


class Solution:

    # hashmap (dictionary)

    def canPermutePalindrome(self, s: str) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1

        count = 0
        for val in dic.values():
            count += val % 2

        if count > 1:
            return False

        return True

    # Set
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        res = set()
        for i in s:
            if i in res:
                res.remove(i)
            else:
                res.add(i)

        return len(res) <= 1
