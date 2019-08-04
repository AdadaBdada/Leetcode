# 49. Group Anagrams
# tuple(sorted('ansa')) -> ('a', 'a', 'n', 's')
# sorted(tuple('ansa')) -> ['a', 'a', 'n', 's']
# tuple immutable
import collections


class Solution:

    # 1. Categorize by Sorted String
    def groupAnagrams1(self, strs):
        '''
        Time Complexity: O(NKlogK),
                         where N is the length of strs, and K is the maximum length of a string in strs.
                         The outer loop has complexity O(N) as we iterate through each string.
                          Then, we sort each string in O(KlogK) time.
        Space Complexity: O(NK)O(NK), the total information content stored in ans.
        '''

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams2(self, strs):
        '''
        Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs.
                         Counting each string is linear in the size of the string, and we count every string.
        Space Complexity: O(NK), the total information content stored in ans.
        '''

        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == "__main__":

    s = Solution()

    res = s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
