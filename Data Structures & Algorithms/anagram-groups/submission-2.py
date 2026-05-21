class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort strs as key in map and store word there
        results = defaultdict(list[str])
        for word in strs:
            sortedWord = "".join(sorted(word))
            results[sortedWord].append(word)
        return list(results.values())
        