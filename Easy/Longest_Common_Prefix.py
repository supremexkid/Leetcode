# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
#
# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)):
            for word in strs[1:]:
                if len(word) <= i:
                    return first_word[:i]
                elif word[i] != first_word[i]:
                    return first_word[:i]
        return first_word

# obj = Solution()
# result = obj.longestCommonPrefix(["flower","flow","flight"])
# print(result)