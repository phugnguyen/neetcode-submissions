class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # shrink window from left while current char is in the set, and remove the left char from the seen

        # keep track of max length
        result = 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result