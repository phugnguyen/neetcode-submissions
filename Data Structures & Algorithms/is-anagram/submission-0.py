class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for char in s:
            currentCount = characters.get(char, 0)
            characters.update({ char: currentCount + 1 })
        for char in t:
            currentCount = characters.get(char, 0)
            characters.update({ char: currentCount - 1 })
        if self.listAllZero(characters.values()):
            return True
        return False

    def listAllZero(self, nums: List[int]):
        for num in nums:
            if num != 0:
                return False
        return True