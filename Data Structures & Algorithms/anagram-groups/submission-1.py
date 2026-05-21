class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict to store Counter with key being idx of results list
        # compare copy
        anagrams = {}
        results = []

        # iterate through strs
        # if anagrams empty, just add to anagrams
        for s in strs:
            countDict = Counter(s)
            if len(results) == 0:
                anagrams[0] = countDict
                results.append([s])
            else:
                anagramFound = False
                for idx, t in enumerate(results):
                    if self.isAnagram(anagrams[idx].copy(), s):
                        results[idx].append(s)
                        anagramFound = True
                if not anagramFound:
                    results.append([s])
                    anagrams[len(results) - 1] = countDict
        return results



    def isAnagram(self, target: Dict[str, int], s: str) -> bool:
        for char in s:
            if char in target and target[char] > 0:
                target[char] -= 1
            else:
                return False

        for val in target.values():
            if val != 0:
                return False
        return True