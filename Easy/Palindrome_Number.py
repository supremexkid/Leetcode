# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# https://leetcode.com/problems/palindrome-number/description/

class Solution:
   def isPalindrome(self, x: int) -> bool:
        result = list(str(x))

        for i in range(len(result)):
            if result[i] != result[-1 - i]:
                return False
        else:
            return True

# obj = Solution()
# result = obj.isPalindrome(121)
# print(result)