class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # user a counter dict
        counted = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for key, val in counted.items(): 
            bucket[val].append(key)
        
        results = []
        for items in reversed(bucket):
            for item in items:
                results.append(item)
                k -= 1
                if k == 0:
                    return results


