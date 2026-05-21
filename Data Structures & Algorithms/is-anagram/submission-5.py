class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCollection = collections.Counter(s)
        tCollection = collections.Counter(t)
        return sCollection == tCollection