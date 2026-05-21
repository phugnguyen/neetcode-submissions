class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums = [1]

        # result = [[], [1]]
        result = []

        subset = []

        def dfs(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()
            dfs(idx + 1)            

        dfs(0)

        return result

