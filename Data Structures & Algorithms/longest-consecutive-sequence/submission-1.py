class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # look for start of sequence, then start the count from there
        items = set(nums)
        starts = []
        for num in nums:
            if num - 1 not in items:
                starts.append(num)

        maxCount = 0
        for start in starts:
            count = 0
            current = start
            while current in items:
                count += 1
                current += 1
            maxCount = max(maxCount, count)

        return maxCount