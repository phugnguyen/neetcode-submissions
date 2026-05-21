class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # turn s into a counter map
        # iterate through t and decrement found characters if > 0
        # else return false
        # return true

        seen = Counter(s)
        for char in t:
            if char in seen and seen[char] > 0:
                seen[char] -= 1
            else:
                return False
        for key, val in seen.items():
            if val != 0:
                return False
        return True

