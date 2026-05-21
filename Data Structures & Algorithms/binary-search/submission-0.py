class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use left and right pointer
        # compare number in the middle to target
        # shift pointers if number not found
        left = 0
        right = len(nums) - 1
        while left <= right:
            current = (left + right)//2
            num = nums[current]
            if target > num:
                left = current + 1
            elif target < num:
                right = current - 1
            else:
                return current
        return -1