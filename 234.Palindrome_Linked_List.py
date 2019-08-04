# 234. Palindrome Linked List


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow = fast = head
        stack = []

        while fast and fast.next:

            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # edge case when odd
        # 当是奇数的时候，fast在倒数第二位，slow 跳过中间位
        if fast:
            slow = slow.next

        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next

        return stack == []
