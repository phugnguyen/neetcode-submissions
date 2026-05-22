class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        memory = set()
        while right < len(s):
            if s[right] not in memory:
                longest = max(longest, right - left + 1)
                memory.add(s[right])
                right += 1
            else:
                while s[right] in memory:
                    memory.remove(s[left])
                    left += 1
        return longest