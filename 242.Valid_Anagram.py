# 242. Valid Anagram
# Python 3


class Solutions:

    # dictionary
    def isAnagram1(self, s: str, t: str) -> bool:

        # edge case
        if len(s) != len(t):
            return False

        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1

        for j in t:
            dic[j] = dic.get(j, -1) - 1

        for value in dic.values():
            if value < 0:
                return False
        return True

    # list count
    def isAnagram2(self, s: str, t: str) -> bool:

        # edge case
        if len(s) != len(t):
            return False

        # check the count of char in s and t equal or not
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
