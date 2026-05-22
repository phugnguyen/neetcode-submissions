class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  shrink when diff in count is >= k
        count = defaultdict(int)
        left = 0
        longest = 0
        for right in range (len(s)):
            count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

