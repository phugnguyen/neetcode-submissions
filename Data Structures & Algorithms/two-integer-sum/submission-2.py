class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # { [target - num]: index }
        d = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], idx]
            else:
                d[num] = idx