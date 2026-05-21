class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive
        # ignore non-alphanumeric
        # .isalnum()
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left >= len(s) or right < 0:
                return True

            leftLowered = s[left].lower()
            rightLowered = s[right].lower()
            if leftLowered != rightLowered:
                return False
            left += 1
            right -= 1
        return True


