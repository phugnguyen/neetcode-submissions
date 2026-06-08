class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # save diff to map with key as indicy to return
        diffMap = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diffMap:
                return sorted([idx, diffMap[diff]])
            diffMap[num] = idx