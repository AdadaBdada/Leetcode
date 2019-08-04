# 249. Group Shifted Strings

# 偏移量相同的字符串


import collections


class Solution:

    def groupStrings(self, strings):

        dic = collections.defaultdict(list)

        for s in strings:
            count = []
            for char in s:
                count.append((ord(char) - ord(s[0])) % 26)

            dic[tuple(count)].append(s)

        return dic.values()

    def groupStrings(self, strings):

        dic = collections.defaultdict(list)

        for s in strings:

            tmp = tuple(map(lambda x: (ord(x) - ord(s[0])) % 26, s))
            dic[tmp].append(s)

        return dic.values()


if __name__ == "__main__":

    s = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    res = s.groupStrings(strings)
    print(res)
