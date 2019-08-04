# 9. Palindrome Number


class Solution:

    def isPalindrome(self, x):
        '''
        Time complexity: reverse a string O(N), N is the lenght of the string
                         check O(N)
        '''
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):

        stack = []
        x = str(x)

        mid = len(x)//2

        for i in range(mid):
            stack.append(x[i])

        if len(x) % 2 == 0:

            for val in x[mid:]:
                if val != stack.pop():
                    return False
        else:
            for val in x[mid+1:]:
                if val != stack.pop():
                    return False

        return stack == []


if __name__ == "__main__":

    s = Solution()
    # 0.317s
    print(s.isPalindrome(1234567890987654321))

    # 0.185s
    print(s.isPalindrome2(1234567890987654321))
