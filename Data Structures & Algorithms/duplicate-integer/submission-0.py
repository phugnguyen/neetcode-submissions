class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if seen.get(num):
                return True
            seen.update({num: True})
        return False