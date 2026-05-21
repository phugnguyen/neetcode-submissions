class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        leftPointer = 0
        seen = set(())
        results = []

        while leftPointer < len(strs):
            result = []
            rightPointer = leftPointer + 1
            leftWord = strs[leftPointer]
            if leftWord in seen:
                 leftPointer += 1
            else:
                result.append(leftWord)
                while rightPointer < len(strs):
                    rightWord = strs[rightPointer]
                    if self.isAnagram(leftWord, rightWord):
                        result.append(rightWord)
                        seen.add(rightWord)
                    rightPointer += 1
                leftPointer += 1
                results.append(result)
        return results

    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            total = chars.get(char, 0)
            chars.update({ char: total + 1 })
        for char in t:
            total = chars.get(char, 0)
            chars.update({ char: total - 1})
        if self.isListAllZeroes(chars.values()):
            return True
        return False

    def isListAllZeroes(self, nums: List[int]) -> bool:
        for num in nums:
            if num != 0:
                return False
        return True