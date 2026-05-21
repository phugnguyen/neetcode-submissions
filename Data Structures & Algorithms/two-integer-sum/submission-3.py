class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lol = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in lol:
                return [lol[diff], idx]
            lol[num] = idx